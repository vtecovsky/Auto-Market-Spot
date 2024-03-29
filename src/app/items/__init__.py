__all__ = ["router"]

from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Items"])

# Register all schemas and routes
import src.app.items.routers  # noqa: E402
