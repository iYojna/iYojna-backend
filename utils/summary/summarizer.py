# -*- coding: utf-8 -*-
"""Summary

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Cz4tvMszMPDnEpFOLZWzw3gGMYQ9Z5V
"""

from transformers import pipeline

df = pd.read_csv('/content/drive/MyDrive/AKAM Hackathon/summary_data.csv')

summarizer = pipeline('summarization')

df['Bullets'][3]

df.head()

df['Name']=df['Name'].astype(str).str.lower()

name_query = "study Abroad Loans"
name_query_lower = name_query.lower()

for ind in df.index:
    # print(df['Name'][ind])
    if name_query_lower == df['Name'][ind]:
      article = df['Bullets'][ind]

print(article)

summary = summarizer(article , max_length = 150 , min_length = 50, do_sample = False)

summary

summary_f = summary[0]['summary_text']

import re
import pandas as pd

pat = ('(?<!Dr)(?<!Esq)\. +(?=[A-Z])')

summary_ff = re.sub(pat,'.\n',summary_f)

import pyperclip

lines = summary_ff.split("\n")

for i in range(len(lines)):
    lines[i] = "-" + lines[i]
  
# converts the list of different
# lines to single text
summary_ff = "\n".join(lines)

print(summary_ff)

import pyperclip
def summaryyy():
  for ind in df.index:
    if name_query_lower == df['Name'][ind]:
      article = df['Bullets'][ind]
  
  summary = summarizer(article , max_length = 150 , min_length = 50, do_sample = False)
  summary_f = summary[0]['summary_text']
  pat = ('(?<!Dr)(?<!Esq)\. +(?=[A-Z])')
  summary_ff = re.sub(pat,'.\n',summary_f)
  lines = summary_ff.split("\n")
  for i in range(len(lines)):
    lines[i] = "-" + lines[i]
  
# converts the list of different
# lines to single text
  summary_ff = "\n".join(lines)


  return lines

print(summaryyy())

