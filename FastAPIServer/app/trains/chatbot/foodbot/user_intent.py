import tensorflow as tf
from keras.models import load_model
from keras import preprocessing

from app.trains.chatbot.demobot.chat_intent import IntentModel
from app.trains.chatbot.demobot.preprocess import Preprocess


## 의도 분류 모듈 생성
class UserIntent:
    def __init__(self, model_name, proprocess):
        ## 의도 클래스별 레이블
        self.labels = {0: "인사", 1: "욕설", 2: "주문", 3: "예약", 4: "기타"}
        ## 의도 분류 모델 불러오기
        self.model = load_model(model_name)
        ## 챗봇 Proprocess 객체
        self.p = proprocess

    # 의도 클래스 예측
    def predict_class(self, query):
        ## 형태소 분석
        pos = self.p.pos(query)

        # 문장 내 키워드 추출 및 불용어 제거 후 인덱스로 전환
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordix_sequence(keywords)]

        # 단어 시퀀스 벡터 크기
        from app.configs.global_params import MAX_SEQ_LEN

        # 패딩 처리
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

        # 모델을 활용한 예측, 예측된 값 중 가장 큰 값의 인덱스 반환
        predict = self.model.predict(padded_seqs)
        predict_class = tf.math.argmax(predict, axis=1)

        return predict_class.numpy()[0]

    def intent_test(self):
        p = Preprocess(word2index_dic='/Users/dianakang/NLP/train_tools/dict/chatbot_dict.bin',
                       userdic='/Users/dianakang/NLP/utils/user_dic.tsv')

        intent = IntentModel(model_name='/Users/dianakang/NLP/models/intent/intent_model.h5', proprocess=p)
        query = "오늘 탕수육 주문 가능한가요?"
        predict = intent.predict_class(query)
        predict_label = intent.labels[predict]

        print(query)
        print("의도 예측 클래스 : ", predict)
        print("의도 예측 레이블 : ", predict_label)

