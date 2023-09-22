import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import re
import numpy as np
import urllib
from sklearn.model_selection import train_test_split
from torchtext.legacy import data
from konlpy.tag import Mecab

if __name__ == '__main__':
    # By using pandas, data save
    train_data = pd.read_table('./data/dataset/ratings_train.txt')
    test_data = pd.read_table('./data/dataset/ratings_test.txt')


    # Check the number of datasets
    # print('Check the number of datasets ..')
    print('The number of train reviews : ', len(train_data))
    print('The number of test reviews : ', len(test_data))

    # Check duplications column of document and label
    # print('Check duplications column of document and label ..')
    train_data['document'].nunique(), train_data['label'].nunique()

    # Remove duplications column of document
    # print('Remove duplications the column of document .. ')
    train_data.drop_duplicates(subset=['document'], inplace=True)
    print('The number of train reviews : ', len(train_data))

    # Check the ratio of train and labels
    train_data['label'].value_counts()

    # Check the null value from train set
    print(train_data.isnull().values.any())
    print(train_data.isnull().sum())
    train_data.loc[train_data.document.isnull()]

    # Remove the samples with null value
    train_data = train_data.dropna(how='any')
    print(train_data.isnull().values.any())

    # Remove special characters with regular expression
    train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
    train_data[:5]

    # Change the white space value to Null value and then remove
    train_data['document'] = train_data['document'].str.replace('^ +', "")  # change the white space to empty value
    train_data['document'].replace('', np.nan, inplace=True)
    print(train_data.isnull().sum())
    train_data = train_data.dropna(how='any')

    # Apply same preprocess to test dataset
    test_data.drop_duplicates(subset = ['document'], inplace=True) # remove duplicate value for column of ducument
    test_data['document'] = test_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") # Apply regular expression
    test_data['document'] = test_data['document'].str.replace('^ +', "") # change the white space to empty value
    test_data['document'].replace('', np.nan, inplace=True) # change epmty space to null value
    test_data = test_data.dropna(how='any') # remove the null value
    print('The number of test dataset after preprocess :',len(test_data))

    # Tokenize
    stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']
