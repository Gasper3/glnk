from http import client

from fastapi import FastAPI, HTTPException, Request, responses

from .routers import url_router

app = FastAPI()

app.include_router(url_router.api_router)


@app.exception_handler(HTTPException)
def base_exception_handler(request: Request, exc: HTTPException):
    exc_info = {
        'status_code': exc.status_code,
        'message': client.responses[exc.status_code],
        'detail': exc.detail
    }
    return responses.JSONResponse(status_code=exc.status_code, content=exc_info)
