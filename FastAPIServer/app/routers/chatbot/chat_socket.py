from typing import List
import tensorflow as tf
from fastapi import WebSocket, APIRouter
from fastapi.responses import HTMLResponse

from keras_preprocessing.sequence import pad_sequences
from starlette.websockets import WebSocketDisconnect
from keras.models import load_model

from app.configs.global_params import MAX_SEQ_LEN
from app.configs.path import dir_path
from app.trains.chatbot.chat_intent import IntentModel
from app.trains.chatbot.food_preprocess import Preprocess

router = APIRouter()
food_router = APIRouter()
html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Hello WebSocket</title>
    <link href="<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<style>
body {
    background-color: #f5f5f5;
}

#main-content {
    max-width: 940px;
    padding: 2em 3em;
    margin: 0 auto 20px;
    background-color: #fff;
    border: 1px solid #e5e5e5;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
}
</style>

</head>
<body>
<h4 style="color: #ff0000">채팅창</h4>
 <h2>Your ID: <span id="ws-id"></span></h2>
<div id="main-content" class="container">
    <div class="row">
        <div class="col-md-6">
            <form class="form-inline" onsubmit="sendMessage(event)">
                <div class="form-group">
                    <input type="text" id="messageText" autocomplete="off"/>
                    <button>Send</button>
                </div>
            </form>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">

                    <h3>메세지</h3>

                <ul id="messages">
                </ul>

        </div>
    </div>
</div>
    <script>
        var client_id = Date.now()
        document.querySelector("#ws-id").textContent = client_id;
        var ws = new WebSocket(`ws://localhost:8000/food/ws/${client_id}`);
        ws.onmessage = function(event) {
            var messages = document.getElementById('messages')
            var message = document.createElement('li')
            var content = document.createTextNode(event.data)
            message.appendChild(content)
            messages.appendChild(message)
        };
        function sendMessage(event) {
            var input = document.getElementById("messageText")
            ws.send(input.value)
            input.value = ''
            event.preventDefault()
        }
    </script>
</body>
"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.get("")
async def get():
    return HTMLResponse(html)


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

@food_router.get("")
async def get():
    return HTMLResponse(html)
@food_router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"Client ask: {data}", websocket)
            res = food_intent(data)
            await manager.broadcast(f"Server #{client_id} answer: {res}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

def food_intent(query: str):
    p = Preprocess(word2index_dic=f'{dir_path("train_tools/dict")}/chatbot_dict.bin',
                   userdic=f'{dir_path("train_tools/dict")}/user_dic.tsv')
    print(f"query : {query}")
    intent = IntentModel2(model_name=f"{dir_path('models/chatbot')}/foodbot_intent.h5", proprocess=p)
    predict = intent.predict_class(query)
    print("의도 예측 클래스 : ", predict)
    predict_label = intent.labels[predict]
    print("의도 예측 레이블 : ", predict_label)
    return predict_label

def food_intent2(query: str):

    print(f"query : {query}") # query = "오늘 탕수육 주문 가능한가요?"
    intent_labels = {0: "인사", 1: "욕설", 2: "주문", 3: "예약", 4: "기타"}

    model = load_model(f'{dir_path("models/chatbot")}/foodbot_intent.h5')
    print("intent 다음 ...")
    p = Preprocess(word2index_dic=f'{dir_path("train_tools/dict")}/chatbot_dict.bin',
                   userdic=f'{dir_path("train_tools/dict")}/user_dic.tsv')
    pos = p.pos(query)
    print(f"pos ...{pos}")
    keywords = p.get_keywords(pos, without_tag=True)
    print(f"keywords ...{keywords}")
    seq = p.get_wordidx_sequence(keywords)
    print(f"seq ...{seq}")
    sequences = [seq]
    print(f"sequences ...{sequences}")
    # 단어 시퀀스 벡터 크기
    padded_seqs = pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')
    print(f"padded_seqs ...{padded_seqs}")
    predict = model.predict(padded_seqs)
    print("의도 예측 점수 : ", predict)
    predict_class = tf.math.argmax(predict, axis=1)
    print("의도 예측 클래스 : ", predict_class.numpy())
    res = intent_labels[predict_class.numpy()[0]]
    print(f"의도 결과  : {res}")
    return res


class IntentModel2:
    def __init__(self, model_name, proprocess):
        # 의도 클래스 별 레이블
        self.labels = {0: "인사", 1: "욕설", 2: "주문", 3: "예약", 4: "기타"}

        # 의도 분류 모델 불러오기
        self.model = load_model(model_name)

        # 챗봇 Preprocess 객체
        self.p = proprocess

    # 의도 클래스 예측
    def predict_class(self, query):
        # 형태소 분석
        pos = self.p.pos(query)

        # 문장내 키워드 추출(불용어 제거)
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordidx_sequence(keywords)]

        # 단어 시퀀스 벡터 크기

        # 패딩처리
        padded_seqs = pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

        predict = self.model.predict(padded_seqs)
        predict_class = tf.math.argmax(predict, axis=1)
        return predict_class.numpy()[0]