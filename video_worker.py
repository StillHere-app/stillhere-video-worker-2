import os
import subprocess
import uuid
import requests

def download_file(url, destination):
    """Download a file from a URL."""
    r = requests.get(url, stream=True)
    with open(destination, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    return destination


def process_video(video_url, persona_id):
    """Download and process the video using FFmpeg."""
    print("[video_worker] Downloading video:", video_url)

    input_filename = f"input_{uuid.uuid4()}.mp4"
    output_filename = f"output_{uuid.uuid4()}.mp4"

    download_file(video_url, input_filename)

    print("[video_worker] Running FFmpeg processing...")

    # Example FFmpeg: re-encode to MP4 H.264
    cmd = [
        "ffmpeg",
        "-i", input_filename,
        "-vcodec", "libx264",
        "-preset", "medium",
        output_filename
    ]

    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("[video_worker] Processing complete:", output_filename)

    # In real usage, upload to cloud storage here
    # For now, return output filename
    return output_filename
