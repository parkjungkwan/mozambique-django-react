import numpy as np
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.saving.save import load_model
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
import os

class FashionService(object):
    def __init__(self):
        pass

    def service_model(self, features): # features = []
       pass


menu = ["Exit", #0
                "service_model"] #1
menu_lambda = {
    "1" : lambda x: x.service_model(),
}
if __name__ == '__main__':
    service = FashionService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                menu_lambda[menu](service)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")