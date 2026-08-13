from pydantic import BaseModel
from datetime import datetime

class AssetBase(BaseModel):
    name: str
    asset_type: str
    estimated_value: float

class AssetCreate(AssetBase):
    pass

class AssetResponse(AssetBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True