import pandas as pd

# 매핑 테이블을 불러옵니다.
mapping = pd.read_csv("python/movie_detail.csv")

# 위 데이터를 불러옵니다.
ratings = pd.read_csv("python/ratings_small.csv")

# 'movieId'를 'id'로 매핑합니다.
ratings['new_movie_id'] = ratings['movieId'].map(
    mapping.set_index('id')['id']).fillna(method='ffill')

# 'movieId' 열을 삭제하고 'new_movie_id' 열을 'movieId'로 이름을 변경합니다.
ratings = ratings.drop('movieId', axis=1).rename(
    columns={'new_movie_id': 'movieId'})

# 결과 확인
print(ratings.head())
