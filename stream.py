import streamlit as st

st.title('멋진 앱')

st.header("메인 콘텐츠 섹션")

col1, col2 = st.columns([1, 2]) # 1:2 비율의 두 열

with col1:
    st.subheader("사이드 패널")
    st.write("왼쪽 열 내용입니다.")

with col2:
    st.subheader("주요 정보")
    st.write("오른쪽 열 내용입니다.")

with st.expander("자세히 보기"):
    st.write("여기에 숨겨진 정보가 있습니다.")

with st.sidebar:
    st.write("사이드바 메뉴")
    st.button("설정")