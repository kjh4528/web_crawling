import streamlit as st
import datetime
import pandas as pd
import json

# 상태 관리(session state)

st.header('세션 상태 예제')

# 'counter' 변수 초기화
if 'count' not in st.session_state:
    st.session_state.count = 0

st.write('현재 카운트',st.session_state.count)

# 버튼 클릭 시 카운트 증가 함수
def increment_counter():
    st.session_state.count += 1

# 버튼 생성 (콜백 함수 연결)
st.button('카운트 증가',on_click=increment_counter)

# 사용자 입력 유지
user_name = st.text_input('이름을 입력하세요',key='name_input')
st.write(f'안녕하세요,{st.session_state.name_input}님!')



##########주요 웨젯(사용자로부터 입력받아 동작 제어)###############

# 텍스트 입력
name = st.text_input('이름을 입력하세요','홍길동')
st.write(f'안녕하세요 {name}님')

# 숫자 입력
# min_value 최소값, max_value 최댓값
age = st.number_input('나이를 입력하세요',min_value=0,max_value=50)
st.write(f'선택된 난이도 : {age}')

#슬라이더(최솟값,최댓값,기본 설정값)
level = st.slider('난이도 선택',1,10,5)
st.write(f'선택된 난이도:{level}')

#드롭다운(단일 선택)
fruit = st.selectbox('좋아하는 과일은?',('사과','바나나','오렌지'))
st.write(f'선택된 과일:{fruit}')

# 다중 선택
colors = st.multiselect("좋아하는 색상", ["빨강", "파랑", "초록",
"노랑"])
st.write(f"선택된 색상: {', '.join(colors)}")

#체크박스
agree = st.checkbox('동의')
if agree:
    st.write('동의 완료')

#날짜 선택
today = st.date_input('오늘 날짜',datetime.date.today())
st.write(f'선택된 날짜:{today}')



##################출력 위젯#############################

#일반 출력
st.write('Hello')
st.write({'key':'value','list':{1,2,3}})

#일반 텍스트
st.text('일반 텍스트')

#마크다운
st.markdown("## 마크다운 제목\n**볼드체** 텍스트와 *이탤릭체* 텍스트")

#데이터 프레임
df = pd.DataFrame({'cool':[1,2],'col2':[3,4]})
st.dataframe(df)

#json 데이터
data = {'name':'Alice','age':30}
st.json(data)
