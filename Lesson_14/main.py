from fastapi import FastAPI, Depends, HTTPException, APIRouter
from starlette.requests import Request

app = FastAPI()

# yield
async def get_async_session():
    print("Получение сессии")
    session = "session"
    yield session
    print("Уничтожение сессии")


@app.get("/items")
async def get_items(session=Depends(get_async_session)):
    print(session)
    return [{"id": 1}]


# parameters
def pagination_params(limit: int = 10, skip: int = 0):
    return {"limit": limit, "skip": skip}


@app.get("/subjects")
async def get_subjects(pagination_params: dict = Depends(pagination_params)):
    return pagination_params


# class
class Paginator:
    def __init__(self, limit: int = 10, skip: int = 0):
        self.limit = limit
        self.skip = skip


@app.get("/subjects_class")
async def get_subjects_class(pagination_params: Paginator = Depends()):
    return pagination_params


# dependencies = [Depends(...)]
# class call
# request

class AuthGuard:
    def __init__(self, name: str):
        self.name = name

    def __call__(self, request: Request):
        if "super_cookie" not in request.cookies:
            raise HTTPException(status_code=403, detail="Запрещено")
        # проверяем что в куках есть инфа о наличии прав пользователя
        return True


auth_guard_payments = AuthGuard("payments")


router = APIRouter(
    dependencies=[Depends(auth_guard_payments)]
)


@app.get("/payments")
def get_payments():
    return "my payments...."

