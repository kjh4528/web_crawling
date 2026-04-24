# sys를 이용하여 하나의 스크립트처럼 사용하기

# 파일 내용 읽는 스크립트
# 코드로 특정 파일 지정하면 매번 수정해야하는 번거로움이 있음
# 스크립트를 만들어 두면 어떤 파일이든 이름만 알려주면 내용을 읽는 뷰어처럼 사용 가능 

 
import sys
if len(sys.argv) > 1: # [0]은 스크립트 파일이므로 1개 이상 입력되어야 함
    filename = sys.argv[1] # [1]파일 이름 저장
    file = open(filename, 'r',encoding='utf8') # 해당 파일 읽기
    text_str = file.read() # 전체 내용 문자열
    print(text_str) # 해당 파일 내용 읽기
    file.close()
