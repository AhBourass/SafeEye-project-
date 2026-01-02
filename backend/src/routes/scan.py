from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_scans():
    return {"message": "Scan route working"}
