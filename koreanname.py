import requests
import json

# 발급받은 인증키를 입력해주세요.
client_id = "oI7mo4fORVtvvtVBy6O7"
client_secret = "kL3dLqswAh"

url = "https://openapi.naver.com/v1/papago/n2mt"

text = "Hello, World!"  # 번역할 텍스트

# 파파고 API 호출
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

# 응답 결과 출력
result = json.loads(response.text)
print(response)
print(result)
translated_text = result["message"]["result"]["translatedText"]

print(translated_text)  # 번역된 텍스트 출력
