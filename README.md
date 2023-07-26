# FastAPI Mixer Control API

This API is designed to control a mixer using a serial port connection. It is built using FastAPI and exposes several endpoints to control and monitor the mixer.

## Installation

1. Install FastAPI: `pip install fastapi`.
2. Install Uvicorn, which is an ASGI server to run the FastAPI application: `pip install uvicorn`.

## Running the Application

Run the FastAPI application using Uvicorn with the following command: uvicorn main:app --reload


Replace `main` with the name of your Python file. The `--reload` flag allows the server to restart after code changes.

## API Endpoints

Here are the available API endpoints:

| Command                 | HTTP Method | Endpoint                | Request Payload | Response Payload |
|-------------------------|-------------|-------------------------|-----------------|------------------|
| get_Name                | GET         | /get_name               | None            | `{"name": int}`  |
| set_Speed               | POST        | /set_speed              | `{"speed": int}`| `{"result": int}`|
| get_Speed               | GET         | /get_speed              | None            | `{"speed": int}` |
| get_Speed_Set_Point     | GET         | /get_speed_set_point    | None            | `{"speed_set_point": int}` |
| get_Viscosity_Trend     | GET         | /get_viscosity_trend    | None            | `{"viscosity_trend": int}` |
| start_Mixer             | POST        | /start_mixer            | None            | `{"result": int}`|
| stop_Mixer              | POST        | /stop_mixer             | None            | `{"result": int}`|
| reset                   | POST        | /reset                  | None            | `{"result": int}`|
| start_Weight            | POST        | /start_weight           | None            | `{"result": int}`|
| stop_Weight             | POST        | /stop_weight            | None            | `{"result": int}`|
| get_Weight_Value        | GET         | /get_weight_value       | None            | `{"weight_value": int}`|
| get_Weight_Status       | GET         | /get_weight_status      | None            | `{"weight_status": (bool, bool, bool, bool, bool)}`|

For POST methods, send a JSON payload in the request body. For example, to set speed, send a POST request to `http://localhost:8000/set_speed` with a request body like `{"speed": 120}`.

## Note

This is a basic implementation and does not include error handling and other considerations for a robust API, such as security, rate-limiting, etc. Depending on the use case, you might need to refine and expand it.




