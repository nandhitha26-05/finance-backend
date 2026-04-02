from fastapi import FastAPI
from app.database import engine, Base
from app.routers import user, records, dashboard
from app import models

# create tables
Base.metadata.create_all(bind=engine)

# create FastAPI app
app = FastAPI(title="Finance Dashboard Backend")

# include routers
app.include_router(user.router)
app.include_router(records.router)
app.include_router(dashboard.router)