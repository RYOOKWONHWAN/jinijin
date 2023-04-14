import os
import sys
import requests
import json
import csv
import codecs


# CSV 파일에 저장할 필드명 정의
fieldnames = ["adult", "backdrop_path", "genre_ids", "id", "original_language",
              "original_title", "overview", "popularity", "poster_path", "release_date",
              "title", "video", "vote_average", "vote_count"]

if not os.path.isfile('movie_data.csv'):
    with open('movie_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

# 여기에서 반복문을 시작하세요.
for i in range(1, 500):  # 예제를 위한 임의의 반복문입니다.
    # ... 기존 코드 (예: API 호출)
    url = "https://api.themoviedb.org/3/movie/popular?api_key=3fa3ffb0e633bd85cdc1fe95f442cf6e&language=ko-KR&page=" + \
        str(i)
    print(url)
    res = requests.get(url)
    json_data = res.json()
  # 결과 목록 추출

    results = json_data['results']

   # CSV 파일에 데이터를 추가합니다 ('append' 모드 사용).
    with open('movie_data.csv', mode='a', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for movie in results:
            cleaned_movie = {key: value.replace('\n', ' ').replace('\r', ' ') if isinstance(
                value, str) else value for key, value in movie.items()}
            if 'adult' in cleaned_movie:
                writer.writerow(cleaned_movie)

    print("CSV 파일에 데이터가 추가되었습니다.")
