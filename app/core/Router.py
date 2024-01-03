from api.Base import router as ApiRouter
from fastapi import APIRouter
from views.Base import ViewsRouter

AllRouter = APIRouter()

# API路由
AllRouter.include_router(ApiRouter)

AllRouter.include_router(ViewsRouter)






