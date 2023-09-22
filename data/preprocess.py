import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import re
import numpy as np
import tqdm
import urllib
from sklearn.model_selection import train_test_split
from konlpy.tag import Mecab
from konlpy.tag import Okt

class preprocess:
    def __init__(self):
        # By using pandas, data save
        self.train_data = pd.read_table('./data/dataset/ratings_train.txt')
        self.test_data = pd.read_table('./data/dataset/ratings_test.txt')
        self.stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']
        self.Okt = Okt()

    def dataset_len(self, type: str):  # Check the number of datasets
        if type == 'train':
            print('The number of train reviews : ', len(self.train_data))
        else:
            print('The number of test reviews : ', len(self.test_data))

    def preprocess(self, type: str):
        if type == 'train':
            # Remove duplications column of document
            self.train_data.drop_duplicates(subset=['document'], inplace=True)

            # Remove the samples with null value
            train_data = self.train_data.dropna(how='any')

            # Remove special characters with regular expression
            train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "")
            train_data[:5]

            # Change the white space value to Null value and then remove
            train_data['document'] = train_data['document'].str.replace('^ +',
                                                                        "")  # change the white space to empty value
            train_data['document'].replace('', np.nan, inplace=True)
            print(train_data.isnull().sum())
            train_data = train_data.dropna(how='any')

            return train_data

        else:
            # Apply same preprocess to test dataset
            self.test_data.drop_duplicates(subset=['document'], inplace=True)

            # Remove the samples with null value
            test_data = self.train_data.dropna(how='any')

            # remove duplicate value for column of ducument
            test_data['document'] = self.test_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "")  # Apply regular expression
            test_data[:5]

            test_data['document'] = self.test_data['document'].str.replace('^ +', "")  # change the white space to empty value
            test_data['document'].replace('', np.nan, inplace=True)  # change epmty space to null value
            test_data = test_data.dropna(how='any')  # remove the null value

            return test_data

    def check_duplication(self):  # Check duplications column of document and label
        self.train_data['document'].nunique(), self.train_data['label'].nunique()
        self.test_data['document'].nunique(), self.test_data['label'].nunique()

    def remove_stopword(self, type: str, data):
        if type == 'train':
            X_train = []
            for sentence in tqdm(self.train_data['document']):
                tokenized_sentence = (self.Okt.morphs(sentence, stem=True))  # 토큰화
                stopwords_removed_sentence = [word for word in tokenized_sentence if not word in self.stopwords]  # 불용어 제거
                X_train.append(stopwords_removed_sentence)
            return X_train

        else:
            X_test = []
            for sentence in tqdm(self.test_data['document']):
                tokenized_sentence = self.Okt.morphs(sentence, stem=True)  # 토큰화
                stopwords_removed_sentence = [word for word in tokenized_sentence if not word in self.stopwords]  # 불용어 제거
                X_test.append(stopwords_removed_sentence)
            return X_test

if __name__ == '__main__':
    data = preprocess()

    data.dataset_len('train')
    data.dataset_len('test')

    data.check_duplication()

    data.preprocess('train')
    data.preprocess('test')

    # Check the ratio of train and labels
    data.train_data['label'].value_counts()

    # Check the null value from train set
    print(data.train_data.isnull().values.any())
    print(data.train_data.isnull().sum())
    data.train_data.loc[data.train_data.document.isnull()]

    print('The number of test dataset after preprocess :',len(data.test_data))