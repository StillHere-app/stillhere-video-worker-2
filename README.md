# StillHere Video Worker

This worker handles video processing for the StillHere platform using RunPod Serverless.

## What it does

- Downloads a user-uploaded video
- Processes it with FFmpeg
- Calls back to the StillHere API when processing is complete

## Files

- `handler.py` – RunPod event handler
- `video_worker.py` – FFmpeg wrapper for video processing
- `requirements.txt` – Dependencies
- `Dockerfile` – Container build instructions
