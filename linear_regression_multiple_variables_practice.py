# -*- coding: utf-8 -*-
"""linear regression multiple variables_practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12bFbWHfO352rrAMhKcd8BgIK_t38kie1
"""

pip install word2number

import pandas as pd
import numpy as np
from sklearn import linear_model
import math
from word2number import w2n

df = pd.read_csv("raw.csv")
df

experience_num = []
for i in df.experience:
  if type(i) == str:
    experience_num.append(w2n.word_to_num(i))
  else:
    experience_num.append(0)
experience_num

df.experience = experience_num
#exp_med = math.floor(df.experience.median())
#df.experience = df.experience.fillna(exp_med)

df

test_score_med = math.floor(df['test_score(out of 10)'].mean())
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(test_score_med)
df

reg = linear_model.LinearRegression()
reg.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])

reg.predict([[2,9,6]])

reg.predict([[12,10,10]])