import numpy as np
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.saving.save import load_model
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
import os

from tensorflow import keras


class FashionService(object):
    def __init__(self):
        global class_names
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    # self, i, predictions_array, true_label, img
    def service_model(self) -> []:
        model = load_model(os.path.join(os.path.abspath("save"), "fashion_model.h5"))
        (train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
        predictions = model.predict(test_images)
        i = 20
        predictions_array, true_label, img = predictions[i], test_labels[i], test_images[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap=plt.cm.binary)
        predicted_label = np.argmax(predictions_array)
        print(f"예측한 답 : {predicted_label}")
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel('{} {:2.0f}% ({})'.format(
            class_names[predicted_label],
            100 * np.max(predictions_array),
            class_names[true_label]
        ), color = color)
        plt.show()

    @staticmethod
    def plot_value_array(i, predictions_array, true_label):
        predictions_array, true_label = \
            predictions_array[i], true_label[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        thisplot = plt.bar(range(10),
                           predictions_array,
                           color='#777777')
        plt.ylim([0, 1])
        predicted_label = np.argmax(predictions_array)
        thisplot[predicted_label].set_color('red')
        thisplot[true_label].set_color('blue')



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