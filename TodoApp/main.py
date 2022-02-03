import models
import auth
import todos
import dependencies
from fastapi import FastAPI, Depends
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router,
                   prefix="/todos",
                   tags=["todos"],
                   dependencies=[Depends(dependencies.get_token_header)],
                   responses={418: {"description": "Internal Use Only"}}
                   )
