from fastapi import FastAPI
from pydantic import BaseModel
from Driver import *


app = FastAPI()

class SpeedModel(BaseModel):
    speed: int

@app.get("/get_name")
def get_name():
    return {"name": get_Name()}

@app.post("/set_speed")
def set_speed(speed: SpeedModel):
    return {"result": set_Speed(speed.speed)}

@app.get("/get_speed")
def get_speed():
    return {"speed": get_Speed()}

@app.get("/get_speed_set_point")
def get_speed_set_point():
    return {"speed_set_point": get_Speed_Set_Point()}

@app.get("/get_viscosity_trend")
def get_viscosity_trend():
    return {"viscosity_trend": get_Viscosity_Trend()}

@app.post("/start_mixer")
def start_mixer():
    return {"result": start_Mixer()}

@app.post("/stop_mixer")
def stop_mixer():
    return {"result": stop_Mixer()}

@app.post("/reset")
def reset():
    return {"result": reset()}

@app.post("/start_weight")
def start_weight():
    return {"result": start_Weight()}

@app.post("/stop_weight")
def stop_weight():
    return {"result": stop_Weight()}

@app.get("/get_weight_value")
def get_weight_value():
    return {"weight_value": get_Weight_Value()}

@app.get("/get_weight_status")
def get_weight_status():
    return {"weight_status": get_Weight_Status()}

