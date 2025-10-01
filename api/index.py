import json
import os
import numpy as np
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# -----------------------------
# Enable CORS for all origins
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow any origin
    allow_methods=["*"],   # allow all methods (POST, OPTIONS, etc.)
    allow_headers=["*"],   # allow all headers
)

# -----------------------------
# Load telemetry data once
# -----------------------------
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-latency.json")
with open(file_path, "r") as f:
    telemetry = json.load(f)

# -----------------------------
# POST endpoint for assignment
# -----------------------------
@app.post("/")
async def analyze_latency(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold = body.get("threshold_ms", 180)

    response = {}
    for region in regions:
        # Filter telemetry by region
        data = [rec for rec in telemetry if rec["region"] == region]
        if not data:
            continue

        latencies = [rec["latency_ms"] for rec in data]
        uptimes = [rec["uptime_pct"] for rec in data]

        response[region] = {
            "avg_latency": float(np.mean(latencies)),
            "p95_latency": float(np.percentile(latencies, 95)),
            "avg_uptime": float(np.mean(uptimes)),
            "breaches": sum(1 for l in latencies if l > threshold)
        }

    return response

# -----------------------------
# Optional: GET route for sanity check
# -----------------------------
@app.get("/")
def root():
    return {"message": "POST JSON {regions: [...], threshold_ms: N} to this endpoint"}
