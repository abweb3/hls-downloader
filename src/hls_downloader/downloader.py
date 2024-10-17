# src/hls_downloader/downloader.py

import yt_dlp
import logging
import os
from pathlib import Path

def download_video(
    url: str,
    output: str = "downloaded_audio",
    headers: dict = None,
    cookiefile: str = None,
    verbose: bool = False,
    audio_only: bool = False,
    audio_format: str = "mp3",
):
    """
    Download video or audio from a given m3u8 URL.

    Args:
        url (str): The m3u8 URL.
        output (str): Output file path without extension (for audio).
        headers (dict, optional): HTTP headers to include.
        cookiefile (str, optional): Path to a cookies file.
        verbose (bool, optional): Enable verbose output.
        audio_only (bool, optional): If True, download only audio.
        audio_format (str, optional): Desired audio format.
    """
    # Define the output template
    if audio_only:
        # Use the specified audio format as the extension
        output_template = Path(output).with_suffix(f".{audio_format}").as_posix()
    else:
        output_template = output

    ydl_opts = {
        'outtmpl': output_template,
        'format': 'best',
        'noplaylist': True,
    }

    if audio_only:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': audio_format,
                'preferredquality': '192',
            }],
            'postprocessor_args': [
                '-ar', '44100'  # Optional: Resample audio to 44.1kHz
            ],
            'prefer_ffmpeg': True,
            'keepvideo': False,
        })

    if verbose:
        ydl_opts['verbose'] = True
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if headers:
        ydl_opts['http_headers'] = headers

    if cookiefile:
        ydl_opts['cookiefile'] = cookiefile

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
