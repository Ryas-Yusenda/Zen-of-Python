from fastapi.responses import FileResponse
from fastapi import FastAPI
from routes.student import student_router
import uvicorn
import os

app = FastAPI()
# uvicorn main:app --reload

favicon_path = 'favicon.ico'

@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)

# Register routes
app.include_router(student_router)

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5000

    os.system("start \"\" http://" + host + ":" + str(port) + "/docs")
    uvicorn.run("main:app", host=host, port=port, reload=True)
