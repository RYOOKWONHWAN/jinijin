import openpyxl
import os
import sys
import requests
import json
import csv
import codecs
from openpyxl.utils.cell import column_index_from_string

fieldnames = ["movie_id", "adult", "gender", "id", "known_for_department", "name", "original_name",
              "popularity", "profile_path", "cast_id", "character", "credit_id", "order"]
if not os.path.isfile('cast_data.csv'):
    with open('cast_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
# 엑셀 파일 열기 (read-only 모드)
workbook = openpyxl.load_workbook('data/movie_list.xlsx', read_only=True)

# 원하는 시트 선택
worksheet = workbook['Sheet1']
# 특정 열 선택 (예시로 B열을 선택)
column_letter = 'C'
column_data = []
for row in worksheet.iter_rows():
    column_data.append(row[column_index_from_string(column_letter)-1].value)

# column_data에는 선택한 열의 데이터가 리스트 형태로 저장됩니다.
print(len(column_data))
for i in range(1, len(column_data)):
    url = "https://api.themoviedb.org/3/movie/" + \
        str(column_data[i]) + \
        "/credits?api_key=3fa3ffb0e633bd85cdc1fe95f442cf6e&language=ko-KR"
    res = requests.get(url)
    json_data = res.json()

    results = json_data['cast']
    movie_id = json_data["id"]

   # CSV 파일에 데이터를 추가합니다 ('append' 모드 사용).
    with open('cast_data.csv', mode='a', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for movie in results:

            cleaned_movie = {key: value.replace('\n', ' ').replace('\r', ' ') if isinstance(
                value, str) else value for key, value in movie.items()}
            cleaned_movie['movie_id'] = movie_id
            if movie['known_for_department'] == 'Acting':
                writer.writerow(cleaned_movie)

    print("CSV 파일에 데이터가 추가되었습니다.")
