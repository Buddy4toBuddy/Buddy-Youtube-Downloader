import os
import subprocess

from pytube import Playlist, YouTube

# # Define the URL of the YouTube playlist
# playlist_url = "https://youtu.be/-RsSl6WtTkM?list=PLI9ofs-2yM9QwRRpin8B60wIzdMZPr1Bl"
# # 'https://youtu.be/faLdQRF2DQk?list=PLnO8uDr9uT6ElC8hlIP-ndsczB1ahdtw3'
# # 'https://youtu.be/RLzC55ai0eo'
#
#
#


from pytube import Playlist, YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import os


# def sanitize_file(filename):
#     # Remove special characters and spaces from the filename
#     return "".join(c for c in filename if c.isalnum() or c in ['-', '_', ' ', '.'])


import os
from pytube import YouTube, Playlist


# Function to get the video and audio streams based on resolution
def get_streams(youtube_url, resolution_choice):
    try:
        yt = YouTube(youtube_url)

        # Get available video streams
        video_streams = yt.streams.filter(adaptive=True, file_extension="webm").order_by('resolution').desc()
        selected_video_stream = video_streams[resolution_choice]
        print('Video streams', selected_video_stream)

        # Get available audio streams
        audio_streams = yt.streams.filter(only_audio=True).order_by('abr').desc()
        selected_audio_stream = audio_streams[0]  # Choose the highest quality audio

        return selected_video_stream, selected_audio_stream

    except Exception as e:
        print("Error:", str(e))
        return None, None


# Function to download and merge video and audio streams
def download_and_merge_video(youtube_url, output_folder, resolution_choice):
    try:
        selected_video_stream, selected_audio_stream = get_streams(youtube_url, resolution_choice)

        if selected_video_stream and selected_audio_stream:
            # Create a folder for the downloaded files if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)

            # Download video and audio streams
            video_path = os.path.join(output_folder, f"video_{resolution_choice}.webm")
            audio_path = os.path.join(output_folder, f"audio_{resolution_choice}.webm")

            selected_video_stream.download()
            selected_audio_stream.download()

            # Define the output file path
            video_title = selected_video_stream.title
            output_file_path = os.path.join(output_folder, f"{video_title}.mp4")

            # Merge video and audio using FFmpeg
            command = [
                'ffmpeg',
                '-i', video_path,
                '-i', audio_path,
                '-c:v', 'libx264',
                '-c:a', 'aac',
                '-strict', 'experimental',
                '-y',  # Overwrite output file if it exists
                output_file_path
            ]

            os.system(' '.join(command))

            print(f"Merged video: {output_file_path}")

            # Clean up: delete the downloaded video and audio files
            os.remove(video_path)
            os.remove(audio_path)

        else:
            print("Video or audio streams not found.")

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLI9ofs-2yM9QwRRpin8B60wIzdMZPr1Bl"
    output_file_path = os.path.join(os.path.expanduser("~"), "Desktop")    # # Specify the folder where you want to save the converted videos
    resolution_choice = int(
        input("Enter the number of the resolution you want to download (e.g., 0 for highest quality): "))

    # Load the playlist and iterate through video URLs
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        download_and_merge_video(video_url, output_file_path, resolution_choice)












