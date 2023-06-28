from http import client

from fastapi import FastAPI, HTTPException, Request, responses, status

from .routers import url_router

app = FastAPI(title='Glnk', version='0.1.0')

app.include_router(url_router.api_router)


@app.exception_handler(HTTPException)
def base_exception_handler(request: Request, exc: HTTPException):
    exc_info = {'status_code': exc.status_code, 'message': client.responses[exc.status_code], 'detail': exc.detail}
    return responses.JSONResponse(status_code=exc.status_code, content=exc_info)


@app.exception_handler(Exception)
def internal_exception_handler(request: Request, exc: Exception):
    exc_info = {'status_code': client.INTERNAL_SERVER_ERROR, 'message': client.responses[client.INTERNAL_SERVER_ERROR]}
    return responses.JSONResponse(status_code=client.INTERNAL_SERVER_ERROR, content=exc_info)
