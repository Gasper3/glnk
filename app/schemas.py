from pydantic import BaseModel, HttpUrl
import typing as t


class UrlRequest(BaseModel):
    url: HttpUrl
    redirect: bool = False


class UrlResponse(BaseModel):
    url: HttpUrl


class ShortUrlResponse(BaseModel):
    short_url: str


class ErrorSchema(BaseModel):
    status_code: int
    message: str


class BadRequestSchema(ErrorSchema):
    detail: str
