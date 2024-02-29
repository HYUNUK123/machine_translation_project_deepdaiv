import pandas as pd
import re

# CSV 파일 불러오기
df = pd.read_csv('result_data/sentence_data.csv')

# print(df['sentence'].str.len()) #5133299문장

# 문자가 10개 보다 적고 100개보다 많은 문장 제거
df_result = df[(10 < df['sentence'].str.len()) & (df['sentence'].str.len() < 100)]
# print(df_result) #3953398문장

# 정규 표현식을 사용하여 알파벳과 숫자가 없는 문장만 필터링
df_result = df_result[df_result['sentence'].str.contains(r'^[^a-zA-Z0-9]+$')]
# print(df_result) #3217616문장

# 한글과 띄어쓰기를 제외한 모든 문자 제거
df_result['sentence'] = df_result['sentence'].apply(lambda x: re.sub(r'[^가-힣\s]','', x))
print(df_result)

df_result.to_csv('./result_data/final_sentence_data.csv',index=False)