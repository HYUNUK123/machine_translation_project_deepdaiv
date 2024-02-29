import json
import pandas as pd
import csv

# JSON 파일 경로
file_path = './Raw_data/animal/BOAN210001637475.json'

# JSON 파일 읽기
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

sentence_data = [sentence["content"] for sentence in data["SJML"]["text"]]

print(sentence_data)

df = pd.DataFrame(sentence_data, columns=['sentence'])

print(df)

df.to_csv('data.csv', index=False)