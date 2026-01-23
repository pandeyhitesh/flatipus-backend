from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.api.routes import (
    auth_routes, house_routes,
    space_routes, task_routes)
from app.shared.database import Base, engine
import os
from dotenv import load_dotenv

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Flatipus API", version="1.0.0")
app.add_middleware(
    SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "supersecretkey"))
app.include_router(auth_routes.router)
app.include_router(house_routes.router)
app.include_router(space_routes.router)
app.include_router(task_routes.router)
