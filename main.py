import os
import pandas as pd
import numpy as np
from typing import List , Any
from fastapi import FastAPI
from fastapi import File, UploadFile , Depends

# import keras


app = FastAPI(
    title = os.environ.get("API_NAME" , "FlyZone API"),
)


try:
    from fastrank.router import rank_router
    app.include_router(router = rank_router , prefix="/rank")
except Exception as e:
    print(e)

try:
    from fastevents.router import events_router
    app.include_router(router = events_router , prefix="/notif")
except Exception as e:
    print(e)

try:
    from fastauth.router import auth_router
    app.include_router(router = auth_router , prefix="/auth")
except Exception as e:
    print(e)





