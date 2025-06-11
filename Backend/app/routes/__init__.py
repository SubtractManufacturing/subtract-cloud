from .items import router as items_router
from .shipments import router as shipments_router

# Export all routers for easier imports
__all__ = ["items_router", "shipments_router"]