# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddlewarex
from app.db.connection.primary_connection import engine, Base
from app.utils.logger import logger



# Initialize FastAPI app
app = FastAPI()