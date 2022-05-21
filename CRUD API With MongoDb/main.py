from fastapi import FastAPI
from routes.student import student_router
import uvicorn
import os

app = FastAPI()
# uvicorn main:app --reload

# Register routes
app.include_router(student_router)

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5000

    os.system("start \"\" http://" + host + ":" + str(port) + "/docs")
    uvicorn.run("main:app", host=host, port=port, reload=True)
