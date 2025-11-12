from fastapi import FastAPI

from .database import Base, engine
from .routers import journal, tasks

app = FastAPI(title="RtaFlow")


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(tasks.router)
app.include_router(journal.router)
