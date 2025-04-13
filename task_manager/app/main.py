from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db, engine, Base
from .routers import tasks
from fastapi.responses import JSONResponse
from sqlalchemy import text
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management System")

app.include_router(tasks.router)

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "detail": str(e)})