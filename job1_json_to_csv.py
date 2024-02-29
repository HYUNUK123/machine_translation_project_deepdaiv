import json
import pandas as pd
import os
import glob

# JSON 파일 경로
directories  = glob.glob('./Raw_data/*')
print(directories) #./Raw_data\\animal

# 모든 JSON 파일의 파일 경로 가져오기
file_paths = []
for directory in directories:
    file_paths.extend([os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith('.json')])
# os.listdir(directory) 함수를 사용하여 현재 디렉터리에 있는 파일 및 디렉터리의 목록을 가져옵니다.
# 각 파일명에 대해 filename.endswith('.json')을 사용하여 확장자가 ".json"인지 확인합니다.
# directory: 디렉터리의 경로를 나타내는 문자열입니다.
# filename: 파일의 이름을 나타내는 문자열입니다.
# directory가 "./Raw_data/subfolder"이고 filename이 "example.json"이라면, os.path.join(directory, filename)은\
# "./Raw_data/subfolder/example.json"과 같은 유효한 파일 경로를 반환합니다.
# print(file_paths)

# 모든 JSON 파일의 "content" 추출
all_sentence_data = []
for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        sentence_data = [sentence["content"] for sentence in data["SJML"]["text"]]
        all_sentence_data.extend(sentence_data)

print(all_sentence_data)

df = pd.DataFrame(all_sentence_data, columns=['sentence'])
#
print(df)
#
df.to_csv('./result_data/sentence_data.csv', index=False)