# データを効率的に扱うライブラリ
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
#from mplfinance import candlestick2_ohlc
from datetime import datetime, timedelta
 
# 自然言語処理（NLP）を扱うライブラリ
import nltk
from nltk.corpus import stopwords
import string
 
# 機械学習ライブラリ
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score
 
# 設定
pd.options.display.max_colwidth = -1
 
# NLTKのモジュールのダウロード
#nltk.download('stopwords')
#nltk.download('punkt')

trump = pd.read_csv('trump.csv')
print(trump.shape)
print(trump.head(2))

# 不要なデータを削除
trump = trump[['created_at', 'text']]
trump.columns = ['time', 'tweet']

# オブジェクトからDatime型へ変換
trump['time'] = pd.to_datetime(trump['time'])
 
# 秒数を四捨五入
trump['time'] = trump['time'].dt.round('min')
 
# 最初の2行を確認
trump.head(2)