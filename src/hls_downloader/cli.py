# src/hls_downloader/cli.py

import click
from .downloader import download_video
import os

@click.command()
@click.option('--url', '-u', prompt='HLS URL', help='The .m3u8 URL to download from.')
@click.option('--output', '-o', default='downloaded_audio', help='Output filename without extension (for audio).')
@click.option('--header', '-H', multiple=True, help='Custom HTTP headers in "Key: Value" format.', type=str)
@click.option('--cookies', '-c', type=click.Path(exists=True), help='Path to cookies file.')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output.')
@click.option('--audio-only', '-a', is_flag=True, help='Download only the audio track.')
@click.option('--audio-format', '-f', default='mp3', type=click.Choice(['mp3', 'm4a', 'aac', 'flac', 'wav', 'ogg']), help='Desired audio format.')
def main(url, output, header, cookies, verbose, audio_only, audio_format):
    """
    HLS Downloader: Download videos or audio from .m3u8 URLs using yt-dlp.
    """
    headers = {}
    for h in header:
        if ':' in h:
            key, value = h.split(':', 1)
            headers[key.strip()] = value.strip()
        else:
            click.echo(f"Invalid header format: {h}. Expected 'Key: Value'.", err=True)
            return

    download_video(
        url=url,
        output=output,
        headers=headers if headers else None,
        cookiefile=cookies,
        verbose=verbose,
        audio_only=audio_only,
        audio_format=audio_format
    )
    final_output = output + f".{audio_format}" if audio_only else output
    click.echo(f"Download completed: {os.path.abspath(final_output)}")
