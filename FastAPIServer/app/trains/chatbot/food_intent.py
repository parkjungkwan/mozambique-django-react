import tensorflow as tf
from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences
# 단어 시퀀스 벡터 크기
from app.configs.global_params import MAX_SEQ_LEN

## 의도 분류 모듈 생성
class FoodIntent:
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

        # 패딩 처리
        padded_seqs = pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

        # 모델을 활용한 예측, 예측된 값 중 가장 큰 값의 인덱스 반환
        predict = self.model.predict(padded_seqs)
        predict_class = tf.math.argmax(predict, axis=1)

        return predict_class.numpy()[0]

