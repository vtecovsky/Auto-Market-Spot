from fastapi import FastAPI

from src.app.auth.base_config import auth_backend, fastapi_users
from src.app.routers import routers
from src.schemas.auth import UserCreate, UserRead

app = FastAPI(title="Auto Market Spot")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


# To clean the database
# @app.on_event("startup")
# async def init_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)

for router in routers:
    app.include_router(router)
