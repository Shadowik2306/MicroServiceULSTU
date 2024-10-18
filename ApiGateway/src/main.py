from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import httpx

services = {
    "web": "http://web:8001",
    "web-report": "http://web-report:8002",
}

app = FastAPI()

async def forward_request(service_url: str, method: str, path: str, body=None, headers=None, params=None):
    async with httpx.AsyncClient() as client:
        url = f"{service_url}{path}"
        if 'content-length' in headers:
            headers.pop('content-length')
        response = await client.request(method, url, json=body, headers=headers, params=params)
        return response


@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def gateway(service: str, path: str, request: Request):
    if service not in services:
        raise HTTPException(status_code=404, detail="Service not found")

    service_url = services[service]
    body = await request.json() if request.method in ["POST", "PUT", "PATCH"] else None
    headers = dict(request.headers)
    params = dict(request.query_params)

    print(headers)
    print(body)
    response = await forward_request(service_url, request.method, f"/{path}", body, headers, params)
    print("Success")
    return JSONResponse(status_code=response.status_code, content=response.json())

@app.get("/")
async def main():
    return {"Hello": "World"}

