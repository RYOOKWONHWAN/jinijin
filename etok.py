import requests
import pandas as pd
from tqdm import tqdm

url = "https://transliterator.herokuapp.com/"
df = pd.read_excel('C:/Users/코딩하는 금융인/Desktop/english_list.xlsx')
sess = requests.Session()
data_list = []

for idx, row in tqdm(df.iterrows()):
    cd_idx = idx+1
    kor_city_name = row['kor_city_name']
    eng_city_name = row['eng_city_name']
    payload = {'input': eng_city_name}
    res = sess.post(url, data=payload)
 # 띄어쓰기 포함될 경우, ?를 뱉어냄 : '?' -&gt; ' ' 바꿔주기
    konglish = res.json()['output'].replace('?', ' ')
    data = {'cd_idx': cd_idx, 'kor_city_name': kor_city_name,
            'eng_city_name': eng_city_name, 'konglish': konglish}
    data_list.append(data)

result_df = pd.DataFrame(
    data_list, columns=['cd_idx', 'kor_city_name', 'eng_city_name', 'konglish'])
result_df.to_excel(
    f'C:/Users/코딩하는 금융인/Desktop/data/result_data.xlsx', index=False)
