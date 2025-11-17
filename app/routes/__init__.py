from app.routes.upload import router as upload_router
from app.routes.get_list import router as list_router
from app.routes.get_detail import router as detail_router

routes = [
    upload_router,
    list_router,
    detail_router
]