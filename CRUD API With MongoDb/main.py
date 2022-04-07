from fastapi import FastAPI
from routes.student import student_router

app = FastAPI()
# uvicorn main:app --reload

# Register routes
app.include_router(student_router)
