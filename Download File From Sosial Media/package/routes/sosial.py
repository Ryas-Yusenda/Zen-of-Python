from fastapi import APIRouter
from ..schemas.sosial import downloadEntity

student_router = APIRouter()

@student_router.get('/', include_in_schema=False)
async def root():
    return {"responses": 200}

@student_router.get('/api/')
async def get_download(url: str):
    if (len(url) > 0):
        return downloadEntity(url)
    else:
        return {"message": "url is required"}
