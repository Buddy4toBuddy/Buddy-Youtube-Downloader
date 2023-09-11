import os

from moviepy.editor import VideoFileClip, AudioFileClip
from utils.message import video_download_messages
from utils.common import get_split_name, sanitize_filename
import subprocess
import imageio_ffmpeg as ffmpeg  # Imageio's FFmpeg interface
import imageio


def select_video_download(video_stream, audio_stream, title):
    if video_stream and audio_stream:
        try:
            print(video_download_messages['intro_message'])

            # Load the video and audio as clips
            video_clip = VideoFileClip(video_stream.download())
            audio_clip = AudioFileClip(audio_stream.download())

            # Set the audio of the video clip to the downloaded audio clip
            video_clip = video_clip.set_audio(audio_clip)

            # Sanitize the title to remove special characters and spaces
            title = get_split_name(title)
            print("title", title)
            sanitized_title = sanitize_filename(title[1])

            # Specify the output file path and codec
            output_file_path = os.path.join(os.path.expanduser("~"), "Desktop", sanitized_title + ".mp4")


            # Write the merged video with the desired frame rate (e.g., 25 fps)
            video_clip.write_videofile(output_file_path, codec="libx264", fps=video_stream.fps)

        except Exception as e:
            print(video_download_messages['wrong_input'], str(e))
    else:
        print(video_download_messages['exception_msg'])

# def select_video_playlist_download(video_stream, audio_stream, title):
#     if video_stream:
#         try:
#             for video_playlist in video_stream:
#                 output_file_path = os.path.join(os.path.expanduser("~"), "Desktop", video_playlist.title)
#                 video_playlist.download(output_file_path)
#                 print(f"Downloaded and merged: {output_file_path}")
#
#         except Exception as e:
#             print(video_download_messages['wrong_input'], str(e))
#     else:
#         print(video_download_messages['exception_msg'])



def select_audio_download(chosen_audio_stream, path):
    if chosen_audio_stream and path:
        try:
            out_file = chosen_audio_stream.download(path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(f"Conversion complete")
        except Exception as e:
            print("Error:", str(e))
    else:
        print("Missing audio stream or output path")

def select_audio_playlist_download(chosen_audio_stream, path):
    if chosen_audio_stream and path:
        try:
            for playlist in chosen_audio_stream:
                out_file = playlist.download(path)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
            print(f"Conversion complete")
        except Exception as e:
            print("Error:", str(e))
    else:
        print("Missing audio stream or output path")



# def sanitize_filenamee(filename):
#     # Remove special characters and spaces from the filename
#     return "".join(c for c in filename if c.isalnum() or c in ['-', '_', ' ', '.'])
#
# def select_video_playlist_download(video_stream, audio_stream, title):
#     try:
#         for video_playlist, audio_playlist in zip(video_stream, audio_stream):
#             print("Downloading video:", video_playlist.title)
#
#             # Sanitize the title to remove special characters and spaces
#             # title = get_split_name(title)
#             # print("title", title)
#             sanitized_title = sanitize_filenamee(video_playlist.title)
#
#             # Download the video and audio streams separately
#             video_stream_file = video_playlist.download()
#             audio_stream_file = audio_playlist.download()
#
#             # Verify if the downloaded files exist
#
#             output_file_path = os.path.join(os.path.expanduser("~"), "Desktop", sanitized_title + ".mp4")
#
#             # Merge audio and video using FFmpeg and save as MP4
#             command = f'ffmpeg -i "{video_stream_file}" -i "{audio_stream_file}"  -c:v copy -c:a aac -strict experimental "{output_file_path}"'
#             os.system(command)
#
#             print(f"Merged video: {output_file_path}")
#
#             # Optionally, you can delete the downloaded video and audio files to save space.
#             # os.remove(video_stream_file)
#             # os.remove(audio_stream_file)
#
#
#     except Exception as e:
#         print("Error:", str(e))






def sanitize_file(filename):
    # Remove special characters and spaces from the filename
    return "".join(c for c in filename if c.isalnum() or c in ['-', '_', ' ', '.'])


def select_video_playlist_download(video_stream, audio_stream, title):
    try:
        for video_playlist, audio_playlist in zip(video_stream, audio_stream):
            print("Downloading video:", video_playlist.title)

            # Sanitize the title to remove special characters and spaces
            sanitized_title = sanitize_file(video_playlist.title)
            print("sanitized_title", sanitized_title)

            # Download the video and audio streams separately
            video_stream_file = VideoFileClip(video_playlist.download())
            audio_stream_file = AudioFileClip(audio_playlist.download())

            # Verify if the downloaded files exist
            print("#$#$$$##2121")
            output_file_path = os.path.join(os.path.expanduser("~"), "Desktop", sanitized_title + ".mp4")

            # Merge audio and video using moviepy
            final_clip = video_stream_file.set_audio(audio_stream_file)

            # Use FFmpeg to save the video with the desired codec
            command = f'ffmpeg -i "{video_stream_file}" -i "{audio_stream_file}"  -c:v copy -c:a aac -strict experimental "{output_file_path}"'
            # Merge audio and video using moviepy, then pipe it to FFmpeg
            final_clip.to_videofile('-', codec="rawvideo").write_videofile(command, verbose=False, logger=None)

            print(f"Merged video: {output_file_path}")
            print("%%%%%")

    except Exception as e:
        print("Error:", str(e))



# def select_video_playlist_download(video_stream, audio_stream, title):
#     try:
#         for video_playlist, audio_playlist in zip(video_stream, audio_stream):
#             print("Downloading video:", video_playlist.title)
#
#             # Sanitize the title to remove special characters and spaces
#             sanitized_title = sanitize_file(video_playlist.title)
#             print("sanitized_title", sanitized_title)
#
#             # Download the video and audio streams separately
#             video_stream_file = video_playlist.download()
#             audio_stream_file = audio_playlist.download()
#
#             # Verify if the downloaded files exist
#             print("#$#$$$##2121")
#             output_file_path = os.path.join(os.path.expanduser("~"), "Desktop", sanitized_title + ".mp4")
#
#             # Merge audio and video using FFmpeg and subprocess
#             print("@@@@@@@@")
#             cmd = [
#                 'ffmpeg',
#                 '-i', video_stream_file,
#                 '-i', audio_stream_file,
#                 '-c:v', 'libx264',
#                 '-c:a', 'aac',
#                 '-strict', 'experimental',
#                 output_file_path
#             ]
#             print("FFmpeg Command:", ' '.join(cmd))
#             try:
#                 subprocess.run(cmd, check=True)
#                 print(f"Merged video: {output_file_path}")
#             except subprocess.CalledProcessError as e:
#                 print(f"Error: {e}")
#
#     except Exception as e:
#         print("Error:", str(e))
