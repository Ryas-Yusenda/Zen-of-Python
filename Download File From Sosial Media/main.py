from fastapi.responses import FileResponse
from fastapi import FastAPI
from package import *
import uvicorn
import os

app = FastAPI()
favicon_path = 'favicon.ico'

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

app.include_router(student_router)

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5000

    os.system("start \"\" http://" + host + ":" + str(port))
    uvicorn.run("main:app", host=host, port=port, reload=True)

"""
TODO: CREATE SECURE ACCOUNT FOR ACCESS API
BUG: -
FIXME: -

import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return [response.encode()]

"""
