from typing import Annotated

from fastapi import APIRouter, Path



router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/")
async def list_items(has_spa: bool = None):
    return [
        "Items 1",
        "Items 2",
        "Items 3",
    ]

@router.get("/latest/")
async def get_latest_item(id:int, name:str):
    return {
        "item":{
            "id": id,
            "name": name
        }
    }

@router.get("/{item_id}/")
async def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item":{
            "id":item_id,
        },
    }
