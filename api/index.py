import json
import os
import numpy as np
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response

app = FastAPI()

# Enable CORS globally
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load telemetry data once
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-latency.json")
with open(file_path, "r") as f:
    telemetry = json.load(f)

# Force CORS headers on every response
@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

# Handle preflight requests explicitly
@app.options("/{full_path:path}")
async def preflight(full_path: str):
    return Response(
        status_code=204,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

# Assignment POST endpoint
@app.post("/")
async def analyze_latency(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold = body.get("threshold_ms", 180)

    response = {}
    for region in regions:
        data = [rec for rec in telemetry if rec["region"] == region]
        if not data:
            continue

        latencies = [rec["latency_ms"] for rec in data]
        uptimes = [rec["uptime_pct"] for rec in data]

        response[region] = {
            "avg_latency": float(np.mean(latencies)),
            "p95_latency": float(np.percentile(latencies, 95)),
            "avg_uptime": float(np.mean(uptimes)),
            "breaches": sum(1 for l in latencies if l > threshold),
        }

    # Explicit CORS header for grader
    return JSONResponse(
        content=response,
        headers={"Access-Control-Allow-Origin": "*"}
    )

# Sanity check GET
@app.get("/")
def root():
    return {"message": "POST JSON {regions: [...], threshold_ms: N} to this endpoint"}
