#!/bin/bash

# =============================================================================
# Example Usage of hls-downloader
# =============================================================================
#
# This script demonstrates various ways to use the `hls-downloader` CLI tool
# to download media from `.m3u8` URLs. It includes examples for:
# - Basic video download
# - Basic audio-only download
# - Audio-only download with specified format
# - Downloads with custom HTTP headers
# - Downloads with cookies
# - Verbose logging
# - Combining multiple options
#
# Ensure that `hls-downloader` is installed and accessible in your PATH.
# Also, make sure FFmpeg is installed on your system for audio extraction.
#
# Usage:
#   ./example_usage.sh
#
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Basic Video Download
# -----------------------------------------------------------------------------
# Downloads the video from the provided `.m3u8` URL and saves it as "video.mp4".
hls-downloader --url "https://example.com/playlist.m3u8" --output "video.mp4"

# -----------------------------------------------------------------------------
# 2. Basic Audio-Only Download (Default Format: mp3)
# -----------------------------------------------------------------------------
# Downloads only the audio from the `.m3u8` URL and saves it as "audio.mp3".
hls-downloader --url "https://example.com/playlist.m3u8" --output "audio.mp3" --audio-only

# -----------------------------------------------------------------------------
# 3. Audio-Only Download with Specified Audio Format
# -----------------------------------------------------------------------------
# Downloads only the audio and saves it in the specified format (e.g., m4a).
# If the output filename does not have an extension, the specified format is appended.
hls-downloader --url "https://example.com/playlist.m3u8" --output "audio" --audio-only --audio-format "m4a"

# -----------------------------------------------------------------------------
# 4. Download with Custom HTTP Headers
# -----------------------------------------------------------------------------
# Adds custom HTTP headers such as "User-Agent" and "Referer" to the request.
hls-downloader -u "https://example.com/playlist.m3u8" \
               -H "User-Agent: Mozilla/5.0" \
               -H "Referer: https://example.com" \
               -o "video_with_headers.mp4"

# -----------------------------------------------------------------------------
# 5. Download with Cookies
# -----------------------------------------------------------------------------
# Uses a cookies file for authenticated streams.
hls-downloader -u "https://example.com/playlist.m3u8" \
               -c "/path/to/cookies.txt" \
               -o "video_with_cookies.mp4"

# -----------------------------------------------------------------------------
# 6. Verbose Video Download
# -----------------------------------------------------------------------------
# Enables verbose logging to provide detailed output during the download process.
hls-downloader -u "https://example.com/playlist.m3u8" \
               -v \
               -o "video_verbose.mp4"

# -----------------------------------------------------------------------------
# 7. Verbose Audio-Only Download
# -----------------------------------------------------------------------------
# Downloads only the audio with verbose logging enabled.
hls-downloader -u "https://example.com/playlist.m3u8" \
               -v \
               -o "audio.mp3" \
               --audio-only

# -----------------------------------------------------------------------------
# 8. Audio-Only Download with Custom Headers and Cookies
# -----------------------------------------------------------------------------
# Combines custom headers and cookies for authenticated audio downloads.
hls-downloader -u "https://example.com/playlist.m3u8" \
               -H "User-Agent: Mozilla/5.0" \
               -H "Referer: https://example.com" \
               -c "/path/to/cookies.txt" \
               -o "audio.mp3" \
               --audio-only

# -----------------------------------------------------------------------------
# 9. Audio-Only Download with Specified Audio Format and Verbose Logging
# -----------------------------------------------------------------------------
# Downloads audio in a specified format (e.g., wav) with verbose logging.
hls-downloader -u "https://example.com/playlist.m3u8" \
               -o "audio" \
               --audio-only \
               --audio-format "wav" \
               -v

# -----------------------------------------------------------------------------
# 10. Download with All Options: Headers, Cookies, Audio-Only, Specified Format, Verbose
# -----------------------------------------------------------------------------
# Combines all available options for a comprehensive download.
hls-downloader -u "https://example.com/playlist.m3u8" \
               -H "User-Agent: Mozilla/5.0" \
               -H "Referer: https://example.com" \
               -c "/path/to/cookies.txt" \
               -o "audio.wav" \
               --audio-only \
               --audio-format "wav" \
               -v

# =============================================================================
# End of example_usage.sh
# =============================================================================
