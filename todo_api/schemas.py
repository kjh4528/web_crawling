# API 요청에서 받을 값/ 응답에서 보여줄 값

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

# BaseModel : 검증 기능을 가진 클래스(필수값,타입 등 검사)
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
    # SQLAlchemy 객체를 Pydantic 응답 모델로 바꾸기
    model_config = ConfigDict(from_attributes=True)


# Base 공통 필드 묶기(생성 요청과 응답에서 공통 사용)
class TodoBase(BaseModel):
    title: str
    description: str | None = None
    is_done: bool = False
    priority: int = Field(..., ge=1, le=3)
    category_id: int

class TodoCreate(TodoBase):
    pass

# patch : 일부 수정 -> 모든 값 선택값 
class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_done: bool | None = None
    priority: int | None = Field(default=None, ge=1, le=3)
    category_id: int | None = None

class TodoResponse(TodoBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
