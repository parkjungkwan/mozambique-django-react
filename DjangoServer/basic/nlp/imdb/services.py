from keras.datasets import imdb
from keras_preprocessing.sequence import pad_sequences
from selenium.webdriver.chrome import webdriver
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

from basic.nlp.imdb.models import ImdbModel


class ImdbService(object):

    def __init__(self):
        global train_input, train_target, test_input, test_target, train_input2, val_input, train_target2, val_target
        (train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)
        train_input2, val_input, train_target2, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

    def hook(self):
        model = ImdbModel()
        # self.show_set()
        # self.target_checker()
        dc = self.txt_length()
        model.create(dc['train_seq'], dc['val_seq'])
        model.fit(train_target, val_target)

    def show_set(self):
        print(train_target[:20])
        print(train_input.shape, test_input.shape)
        print(len(train_input[0]))
        print(train_input[0])

    def target_checker(self):
        print(train_target2[:20])
        lengths = np.array([len(x) for x in train_input2])
        print(f"평균값, 중간값 {np.mean(lengths)}, {np.median(lengths)}")
        plt.hist(lengths)
        plt.xlabel('lengths')
        plt.ylabel('frequency')
        plt.show()

    def txt_length(self):
        train_seq = pad_sequences(train_input, maxlen=100)
        print(train_seq.shape)
        print(train_seq[0])
        print(train_input[0][:-10])
        print(train_seq[5])
        val_seq = pad_sequences(val_input, maxlen=100)
        return {'train_seq':train_seq, 'val_seq':val_seq}


class NaverMovieService(object):
    def __init__(self):
        pass

    def crawling(self):
        url = 'https://movie.naver.com/movie/point/af/list.naver?&page=1'
        driver = webdriver.Chrome(r'C:\Users\AIA\MsaProject\DjangoServer\basic\webcrawler\chromedriver.exe')
        file_name = 'naver_movie_review_corpus.csv'
        driver.close()



if __name__ == '__main__':
    ImdbService().hook()

