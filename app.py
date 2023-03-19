from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from views import blog_router


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(router=blog_router)
