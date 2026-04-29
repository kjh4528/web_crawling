# 과제 요구 사항: POST/GET/DELETE /categories

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

# 카테고리 생성(POST) API
@router.post("", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(get_db),
):
# 새로 만들기 전 같은 이름 카테고리 있는지 확인 
    existing_category = (
        db.query(models.Category)
        .filter(models.Category.name == category.name)
        .first()
    )
# 같은 이름이 있으면 에러 문구 출력(category name unique)
    if existing_category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category name already exists",
        )
# 새 카테고리 모델 객체 만들어 db 저장 
    new_category = models.Category(name=category.name)

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


# 카테고리 전체 조회(GET) API 
@router.get("", response_model=list[schemas.CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


# 카테고리 삭제(DELETE) API
@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
# 삭제하려는 카테고리가 DB에 있는지 조회 
    category = (
        db.query(models.Category)
        .filter(models.Category.id == category_id)
        .first()
    )
# 삭제할 카테고리가 없으면 에러 반환 
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
# 있으면 삭제하고 DB에 반영 
    db.delete(category)
    db.commit()
