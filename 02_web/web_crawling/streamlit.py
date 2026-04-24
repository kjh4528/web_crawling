# streamlit 레이아웃 구성
# 다양한 함수를 활용하여 직관적인 사용자 인터페이스 만들어보기

import streamlit as st

# 제목과 섹션 정의하여 구조 명확화
st.title("나의 멋진 Streamlit 앱")
st.header("메인 콘텐츠 섹션")

# 화면 여러 열로 분할하여 콘텐츠 나란히 배치
col1, col2 = st.columns([1, 2]) # 1:2 비율의 두 열

with col1:
st.subheader("사이드 패널")
st.write("왼쪽 열 내용입니다.")

with col2:
st.subheader("주요 정보")
st.write("오른쪽 열 내용입니다.")

# 접기/펼치기 세션(복잡한 정보 필요한 경우에만 표시)
with st.expander("자세히 보기"):
st.write("여기에 숨겨진 정보가 있습니다.")

# 사이드바에 부가적인 컨트롤 배치 
with st.sidebar:
st.write("사이드바 메뉴")
st.button("설정")
