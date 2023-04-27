import requests
import json
import pandas as pd

# 발급받은 인증키를 입력해주세요.
client_id = "oI7mo4fORVtvvtVBy6O7"
client_secret = "kL3dLqswAh"

url = "https://openapi.naver.com/v1/papago/n2mt"

df = pd.read_csv('python/data_2023-04-24/new_cast_data.csv')
texts = df['name']

translated_texts = []

# 텍스트 번역
for i in range(400, 500):
    text = texts[i]
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }
    data = {
        "source": "en",
        "target": "ko",
        "text": text,
    }
    response = requests.post(url, headers=headers, data=data)
    result = json.loads(response.text)
    translated_text = result["message"]["result"]["translatedText"]
    print(result)
    print(translated_text)
    translated_texts.append(translated_text)
    print(texts[i], '->', translated_text)

# CSV 파일로 저장
translated_df = pd.DataFrame({'korean_name': translated_texts})
with open('korean_cast_data.csv', mode='a', encoding='utf-8-sig', newline='') as f:
    translated_df.to_csv(f, header=f.tell() == 0, index=False)
