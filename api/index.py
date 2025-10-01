import json
import os
import numpy as np
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Load telemetry data once
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-latency.json")
with open(file_path, "r") as f:
    telemetry = json.load(f)

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

        avg_latency = float(np.mean(latencies))
        p95_latency = float(np.percentile(latencies, 95))
        avg_uptime = float(np.mean(uptimes))
        breaches = sum(1 for l in latencies if l > threshold)

        response[region] = {
            "avg_latency": avg_latency,
            "p95_latency": p95_latency,
            "avg_uptime": avg_uptime,
            "breaches": breaches,
        }

    return response

# Optional: GET for browser sanity check
@app.get("/")
def root():
    return {"message": "POST JSON {regions: [...], threshold_ms: N} to this endpoint"}
