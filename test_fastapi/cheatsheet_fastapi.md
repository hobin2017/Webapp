# http
## [raw request](https://fastapi.tiangolo.com/advanced/using-request-directly/)
```python
from fastapi import Request

def func01(request: Request):
    # Request class: https://www.starlette.io/requests/
    return {
        'url': request.url,
        'query_params': request.query_params,
        'headers': request.headers,
        'cookies': request.cookies,
    }
```
## http-method
```python
from fastapi import Request

def func01(request: Request):
    return {'method': request.method}
```

## http-url
### [uri parameter](https://fastapi.tiangolo.com/tutorial/path-params/)
```python
from fastapi import FastAPI

app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
### [query-string](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#import-query)
```python
from fastapi import Query

def func01(
    param01: str = Query(default='')
):
    return locals()  # dict
```

## [http-header](https://fastapi.tiangolo.com/tutorial/header-params/)
```
```

## http-body
### raw body
```python
from fastapi import Request

async def func01(request: Request):
    return {
        'body': await request.body(),
    }
```
### [json](https://fastapi.tiangolo.com/tutorial/body/)
```python
from pydantic import BaseModel

class PutBinding(BaseModel):
    id: str

def func01(binding: PutBinding):
    return binding
```
### form
- [form-submission](https://fastapi.tiangolo.com/tutorial/request-forms/)
```python
from fastapi import Form

def func01(
    username: str = Form(''),
    password: str = Form('')
):
    return locals()
```
- [file-upload](https://fastapi.tiangolo.com/tutorial/request-files/)
```
```

## http-response
### json
```python
def func01():
    return {'key01': 'value01'}
```

# code-segments
## [router](https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter)
```python
from fastapi import FastAPI, APIRouter

func01 = lambda: print(11)
router01 = APIRouter(prefix="/prefix")
#
router02 = APIRouter(prefix="/app01")
router02.add_api_route("/app-info", func01, methods=['GET'])
#
router01.include_router(router02)
app = FastAPI()
app.include_router(router01)
```
## middleware
### [CORS-middleware](https://fastapi.tiangolo.com/tutorial/cors/)
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
```
## [background task](https://fastapi.tiangolo.com/tutorial/background-tasks/)


# concepts
## [model-config](https://pydantic-docs.helpmanual.io/usage/model_config/)
## [validators](https://pydantic-docs.helpmanual.io/usage/validators/)
## [OAuth2](https://fastapi.tiangolo.com/tutorial/security/first-steps/#the-password-flow)
> The password flow is simplified below:
>  - The frontend sends the username and password in http-form format to the backend normally called the login-api.
>  - After verifying the password, the login-api returns a token-value, such as `token-value01`, to the frontend.
>  - The frontend send next request with the token-value in the http-header, such as `Authorization: Bearer token-value01`.
## [/docs url](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs)
