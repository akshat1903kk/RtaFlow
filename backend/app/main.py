from fastapi import FastAPI

from .database import Base, engine
from .routers import admin, admin_dashboard, auth, journal, tasks

app = FastAPI(title="RtaFlow")


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def health_check():
    return {"status": "healthy", "app": "RtaFlow", "test api at": "/docs"}


app.include_router(tasks.router)
app.include_router(journal.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(admin_dashboard.router)
