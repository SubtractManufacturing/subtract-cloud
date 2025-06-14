from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import create_db_and_tables
from .routes.items import router as items_router
from .routes.shipments import router as shipments_router
from .routes.orders import router as orders_router

app = FastAPI(title="Subtract Manufacturing Backend Service")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(items_router, prefix="/api")
app.include_router(shipments_router, prefix="/api")
#app.include_router(orders_router, prefix="/api")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Subtract Manufacturing Backend Service is running!"}