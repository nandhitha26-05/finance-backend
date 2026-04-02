from fastapi import APIRouter

router = APIRouter()

@router.get("/records")
def get_records():
    return {"message": "Records working"}