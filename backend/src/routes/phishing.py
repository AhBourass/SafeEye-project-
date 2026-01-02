from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_phishing_info():
    return {"message": "Phishing route working"}
