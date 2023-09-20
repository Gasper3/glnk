import typing as t


class RequestData(t.TypedDict):
    user_agent: str
    ip_address: str
