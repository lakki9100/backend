from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import places, chat

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(places.router)
app.include_router(chat.router)
