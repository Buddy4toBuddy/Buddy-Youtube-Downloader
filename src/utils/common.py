import os
import re  # Import the re module for regular expressions
from .message import common_file_messages
from pytube import YouTube, Playlist

# File download path
def get_output_path(title):
    return os.path.join(os.path.expanduser("~"), "Desktop", title)

# Audio quality list and user selection
def get_audio_quality_choice(audio_streams):
    print(common_file_messages['audio_quality_availability'])
    for i, stream in enumerate(audio_streams):
        print(f"{i + 1}. {stream.abr} (Audio)")

    while True:
        audio_choice = int(input(common_file_messages['audio_choice']))
        if 1 <= audio_choice <= len(audio_streams):
            return audio_choice
        else:
            print(common_file_messages['exception_msg'])

# Extracting the playlist audio one by one
def get_audio_playlist(url):
    playlist = Playlist(url)
    video = YouTube(url)
    audio_stream = video.streams.filter(only_audio=True).order_by('abr').desc()
    audio_choice = get_audio_quality_choice(audio_stream)
    playlist_list = []  # Initialize a list to store audio streams
    for video_url in playlist.video_urls:
        video = YouTube(video_url)
        audio_stream = video.streams.filter(only_audio=True).order_by('abr').desc()[audio_choice - 1]
        playlist_list.append(audio_stream)
    return playlist_list, playlist

# for the single audio file
def get_audio_single(url):
    audio_streams = YouTube(url)
    audio_streams = audio_streams.streams.filter(only_audio=True).order_by('abr').desc()
    audio_choice = get_audio_quality_choice(audio_streams)
    audio_single_stream = audio_streams[audio_choice - 1]
    return audio_single_stream

# Video quality list and user selection
def get_video_resolution_choice(video_stream):
    print(common_file_messages['video_quality_availability'])
    for i, stream in enumerate(video_stream):
        print(f"{i + 1}. {stream.resolution}")

    while True:
        video_choice = int(input(common_file_messages['video_choice']))
        if 1 <= video_choice <= len(video_stream):
            return video_choice
        else:
            print(common_file_messages['exception_msg'])

# Split the desktop path
def get_split_name(title):
    if '/' in title or '\\' in title:
        title = title.split("Desktop") if "Desktop" in title else title
    return title

# Removing special characters from the video or audio file name
def sanitize_filename(filename):
    # Remove special characters and spaces from the filename
    return re.sub(r'[\\/:"*?<>|]+', '', filename)
