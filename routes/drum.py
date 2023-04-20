from fastapi import APIRouter
from schemas.drum import Drum
from database.dataset import drumDataBase

router = APIRouter(prefix="/drums", tags=["drums"])


@router.get("/")
def getDrums():
    return {"data": drumDataBase}

@router.post("/")
def addDrum(drum: Drum):
    drumDataBase.append(drum.dict())
    return {"data": drumDataBase}

@router.delete("/{drumId}")
def deleteDrum(drumId: int):
    # for drum in drumDataBase:
    #     if drum["id"] == drumId:
    #         drumDataBase.remove(drum)
    #         return {"data": drumDataBase}
    # ! =
    newSet = [drum for drum in drumDataBase if drum["id"] != drumId]
    return {"data": newSet}


@router.get("/{drumName}")
def getSpecificDrum(drumName: str):
    for drum in drumDataBase:
        if drum["name"] == drumName.lower():
            return drum
        
    return {"message": "Found nothing"}
