from api.path import fruits
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.callbacks import ModelCheckpoint
import tensorflow as tf
import tensorflow_datasets as tfds

class FruitsService:
    def __init__(self):

        global class_names, Apple_Braeburn_Test, Apple_Braeburn_Train, \
            Apple_Crimson_Snow_Train, Apple_Golden_1_Train, Apple_Golden_2_Train, \
            Apple_Golden_3_Train, Apple_Crimson_Snow_Test, Apple_Golden_1_Test, \
            Apple_Golden_2_Test, Apple_Golden_3_Test, batch_size, img_height, img_width, \
            trainpath, testpath

        trainpath = f"{fruits}\\fruits-360-5\\Training"
        testpath = f"{fruits}\\fruits-360-5\\Test"
        Apple_Braeburn_Train = f"{trainpath}\\Apple Braeburn"
        Apple_Crimson_Snow_Train = f"{trainpath}\\Apple Crimson Snow"
        Apple_Golden_1_Train = f"{trainpath}\\Apple Golden 1"
        Apple_Golden_2_Train = f"{trainpath}\\Apple Golden 2"
        Apple_Golden_3_Train = f"{trainpath}\\Apple Golden 3"
        Apple_Braeburn_Test = f"{testpath}\\Apple Braeburn"
        Apple_Crimson_Snow_Test = f"{testpath}\\Apple Crimson Snow"
        Apple_Golden_1_Test = f"{testpath}\\Apple Golden 1"
        Apple_Golden_2_Test = f"{testpath}\\Apple Golden 2"
        Apple_Golden_3_Test = f"{testpath}\\Apple Golden 3"
        batch_size = 32
        img_height = 100
        img_width = 100

    def hook(self):
        self.show_apple()
        train_ds = self.create_train_ds()
        validation_ds = self.create_validation_ds()
        test_ds = self.create_test_ds()
        print(f"*** Type of test_ds is {type(test_ds)} ***")
        # Type of test_ds is tensorflow.python.data.ops.dataset_ops.BatchDataset
        test_ds1 = self.create_test_ds1()
        class_names = train_ds.class_names
        self.merge_image_label_tester(test_ds=test_ds,
                               test_ds1=test_ds1,
                               class_names=class_names,
                               index=-1) # -1 은 가장 마지막 인덱스


    def show_apple(self):
        img = tf.keras.preprocessing.image.load_img \
            (f'{Apple_Golden_3_Train}\\0_100.jpg')
        plt.imshow(img)
        plt.axis("off")
        plt.show()

    def create_train_ds(self):
        return tf.keras.preprocessing.image_dataset_from_directory(
            trainpath,
            validation_split=0.3,
            subset="training",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

    def create_validation_ds(self):
        return tf.keras.preprocessing.image_dataset_from_directory(
            trainpath,
            validation_split=0.3,
            subset="validation",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

    def create_test_ds(self):
        return tf.keras.preprocessing.image_dataset_from_directory(
            testpath,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

    def create_test_ds1(self):
        return tf.keras.preprocessing.image_dataset_from_directory(
            testpath,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size,
            shuffle=False) # shuffle=False 데이터셋 test_ds1을 별도로 생성

    def extract_label_from_ds(self, ds):
        return np.concatenate([y for x, y in ds], axis=0)

    def extract_image_info(self, ds):
        return np.concatenate([x for x, y in ds], axis=0)

    def merge_image_label_tester(self, **kwargs):
        test_ds = kwargs["test_ds"]
        test_ds1 = kwargs["test_ds1"]
        class_names = kwargs["class_names"]
        y = self.extract_label_from_ds(test_ds)
        print(f"test_ds에서 레이블 정보만 추출하여 y에 저장\n"
              f"실행할 때마다 y 배열이 변경됨: {y}\n")
        y = self.extract_label_from_ds(test_ds1)
        print(f"Shuffle=False 옵션을 통해 불러온 test_ds1 정보를 y에 저장\n"
              f"실행할 때마다 y 배열이 변경이 없음: {y}\n")
        x = self.extract_image_info(kwargs["test_ds1"])
        print(f"test_ds1에서 이미지 정보만 추출하여 x에 저장 : {x[0]}\n")
        plt.figure(figsize=(3, 3))
        plt.imshow(x[0].astype("uint8"))
        plt.title(class_names[y[0]])
        plt.axis("off")
        plt.show()

    def merge_image_label(self, **kwargs):
        dataset = kwargs["dataset"]
        class_names = kwargs["class_names"]
        i = kwargs["index"]
        x = self.extract_image_info(dataset)
        y = self.extract_label_from_ds(dataset)
        plt.figure(figsize=(3, 3))
        plt.imshow(x[i].astype("uint8"))
        plt.title(class_names[y[i]])
        plt.axis("off")
        plt.show()

if __name__ == '__main__':
    FruitsService().hook()
