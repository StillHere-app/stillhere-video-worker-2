import os
import json
import runpod
from video_worker import process_video

CALLBACK_URL = os.getenv("CALLBACK_URL")
VIDEO_CALLBACK_SECRET = os.getenv("VIDEO_CALLBACK_SECRET")

def handler(event):
    """
    Main handler called by RunPod.
    Downloads the video, processes it using FFmpeg,
    then calls back to the StillHere API.
    """

    print("[handler] Event received:", event)

    job_input = event.get("input", {})
    video_url = job_input.get("video_url")
    persona_id = job_input.get("persona_id")

    if not video_url:
        return {"error": "No video_url provided"}

    print(f"[handler] Processing video for persona {persona_id}")

    output_url = process_video(video_url, persona_id)

    # Prepare callback data
    payload = {
        "persona_id": persona_id,
        "output_url": output_url,
        "secret": VIDEO_CALLBACK_SECRET
    }

    print(f"[handler] Sending callback to {CALLBACK_URL}")

    try:
        import requests
        resp = requests.post(CALLBACK_URL, json=payload)
        print("[handler] Callback response:", resp.text)
    except Exception as e:
        print("[handler] Callback failed:", e)

    return {"status": "processing_complete", "output_url": output_url}


runpod.serverless.start({"handler": handler})
