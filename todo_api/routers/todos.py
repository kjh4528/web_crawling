# POST/GET/GET{id}/PATCH/DELETE /todos

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db


router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)

# Todo 테이블 category_id 필수값 -> 존재하는지 확인 
def get_category_or_404(category_id: int, db: Session):
    category = (
        db.query(models.Category)
        .filter(models.Category.id == category_id)
        .first()
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return category

# Todo 조회,수정,삭제시 반복적 사용 
def get_todo_or_404(todo_id: int, db: Session):
    todo = (
        db.query(models.Todo)
        .filter(models.Todo.id == todo_id)
        .first()
    )

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )

    return todo


# 생성 API 
@router.post("", response_model=schemas.TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo: schemas.TodoCreate,
    db: Session = Depends(get_db),
):
    get_category_or_404(todo.category_id, db)

    new_todo = models.Todo(
        title=todo.title,
        description=todo.description,
        is_done=todo.is_done,
        priority=todo.priority,
        category_id=todo.category_id,
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

# 전체 조회 API, 리스트로 반환 
@router.get("", response_model=list[schemas.TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

# 단건 조회 API 
@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(
    todo_id: int,
    db: Session = Depends(get_db),
):
    return get_todo_or_404(todo_id, db)

# 수정 API 
@router.patch("/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(
    todo_id: int,
    todo_update: schemas.TodoUpdate,
    db: Session = Depends(get_db),
):
    todo = get_todo_or_404(todo_id, db)
    update_data = todo_update.model_dump(exclude_unset=True) # 요청 보낸 값만 수정

    # 카테고리 바꿀 때는 바꿀 id 존재하는지 확인 
    if "category_id" in update_data:
        get_category_or_404(update_data["category_id"], db)
    # 보낸 필드들 Todo 객체에 하나씩 반영 
    for field, value in update_data.items():
        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)

    return todo

# 삭제 API 
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
):
    todo = get_todo_or_404(todo_id, db)

    db.delete(todo)
    db.commit()
