import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import re
import numpy as np
import urllib
import tqdm
from sklearn.model_selection import train_test_split
from konlpy.tag import Mecab
from konlpy.tag import Okt
from preprocess import preprocess
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Tokenize
class Tokenize:
    def __init__(self):
        self.stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']

    def Tokenizer(self, data):
        tokenizer = Tokenizer()
        return tokenizer.fit_on_texts(data)


if __name__ == '__main__':
    data = preprocess()
    token = Tokenize()
    X_train = data.remove_stopword('train')
    X_test = data.remove_stopword('test')
    token = token.Tokenizer(X_train)

