from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

#1. DB 주소 생성
DATABASE_URL = "sqlite:///./todo.db"

#2. engine 생성(fastAPI와 DB사이 연결 장치)
engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread':False})

#3. SessionLocal(DB 세션 생성기)
# session은 DB작업의 작업 단위 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#4. Base 생성(테이블 클래스 만들 때 상속받는 기본 클래스)
Base = declarative_base()

# 라우터에서 DB 세션 쉽게 받도록 하는 함수
def get_db():  # 요청마다 세션을 만들고 닫아주는 관리 
    db = SessionLocal() # db: 실제 DB작업을 하는 세션 객체
    try:
        yield db  # 라우터 함수에 세션 전달
    finally:  # 응답 종료 후 finally 수행-> 세션 닫기 
        db.close()

