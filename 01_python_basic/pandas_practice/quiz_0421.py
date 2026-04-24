# %% 
import pandas as pd
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s['c'])

# %%
import pandas as pd
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'score': [90, 85, 92]}
df = pd.DataFrame(data)
print(df.shape, len(df))
# %%
import pandas as pd
data = {'이름':['김철수','이영희','박지수'],
        '국어':[85, 92, 78],
        '영어':[90, 88, 95],
        '수학':[80, 75, 88]}
df = pd.DataFrame(data)
print(df.head(2))
# %%
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]},
                  index=['x', 'y', 'z'])
print(df.loc['y', 'B'], df.iloc[2, 0])
# %%
import pandas as pd
df = pd.DataFrame({
    'name': ['Kim', 'Lee', 'Park', 'Choi'],
    'score': [85, 92, 78, 95]
})
result = df[df['score'] >= 90]
print(len(result), result['name'].tolist())

# %%
import pandas as pd
data = {'이름': ['Kim', 'Lee', 'Park'],
        '점수': [85, None, 92],
        '등급': ['A', 'B', None]}
df = pd.DataFrame(data)
df = df.fillna(0)
df
# %%
import pandas as pd

df = pd.DataFrame({'score': [70, 80, 90, 85, 75]})
print(df['score'].max(), df['score'].sum(), df['score'].mean())

# %%
import pandas as pd
data = {'이름' : ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    '부서' : ['영업', '개발', '개발', '영업', '인사'],
    '월급' : [280, 350, 420, 310, 260]}
df = pd.DataFrame(data)
print(df[df['월급'] >= 300].sort_values('월급',ascending=False))

# %%
import pandas as pd
data = {'이름' : ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    '부서' : ['영업', '개발', '개발', '영업', '인사'],
    '월급' : [280, 350, 420, 310, 260]}
df = pd.DataFrame(data)
print(df.groupby('부서')['월급'].mean())
# %%
import pandas as pd
data1 = {'학번' : [1001, 1002, 1003, 1004],
    '이름' : ['김철수', '이영희', '박지수', '최민준']}

data2 = {'학번' : [1001, 1002, 1004],
    '국어' : [85, 92, 78],
    '영어' : [90, 88, 82],
    '수학' : [80, 75, 95]}

df_n = pd.DataFrame(data1)
df_s = pd.DataFrame(data2)

merged = pd.merge(df_n,df_s,'left','학번')
merged = merged.fillna(0)
merged['총점'] = merged[['국어','영어','수학']].sum(axis=1)
print(merged[merged['총점'] >= merged['총점'].mean()].sort_values('이름',ascending=True))
# %%
