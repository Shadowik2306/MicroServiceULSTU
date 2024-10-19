from fastapi.responses import JSONResponse
from fastapi import HTTPException

import httpx
from fastapi import Request

services = {
    "web": "http://web:8001",
}

async def forward_request(service_url: str, method: str, path: str, body=None, headers=None, params=None):
    async with httpx.AsyncClient() as client:
        url = f"{service_url}{path}"
        if 'content-length' in headers:
            headers.pop('content-length')
        response = await client.request(method, url, json=body, headers=headers, params=params)
        return response



async def gateway(path: str, request: Request):
    service_url = services["web"]
    body = await request.json() if request.method in ["POST", "PUT", "PATCH"] else None
    headers = dict(request.headers)
    params = dict(request.query_params)

    response = await forward_request(service_url, request.method, f"/{path}", body, headers, params)
    return JSONResponse(status_code=response.status_code, content=response.json())