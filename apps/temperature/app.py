from random import randint
from datetime import datetime, timezone
from fastapi import FastAPI
from typing import Dict


app = FastAPI()

locations = ["Living Room", "Bedroom", "Kitchen"]

SENSOR_TO_LOCATION = {s: l for s, l in enumerate(locations, start=1)}
LOCATION_TO_SENSOR = {l: s for s, l in SENSOR_TO_LOCATION.items()}

def get_random_temperature(min_value: int = -50, max_value: int = 50) -> int:
    return randint(min_value, max_value)

def get_sensor_id_by_location(location: str) -> int:
    return LOCATION_TO_SENSOR.get(location, 0)

def get_location_by_sensor_id(sensor_id: int) -> str:
    return SENSOR_TO_LOCATION.get(sensor_id, "Unknown")

def prepare_response(sensor_id: int, location: str) -> Dict:
    return {
        "value": get_random_temperature(),
        "unit": "°C",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "location": location,
        "status": "ok",
        "sensor_id": str(sensor_id),
        "sensor_type": "temperature",
        "description": "Temperature sensor",
    }


@app.get("/health")
async def health_check() -> Dict:
    return {"status": "ok"}

@app.get("/temperature")
async def get_temperature(location: str) -> Dict:
    sensor_id = get_sensor_id_by_location(location)
    response = prepare_response(sensor_id, location)
    return response

@app.get("/temperature/{sensor_id}")
async def get_temperature_by_sensor_id(sensor_id: int) -> Dict:
    location = get_location_by_sensor_id(sensor_id)
    response = prepare_response(sensor_id, location)
    print(sensor_id, location, response)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
