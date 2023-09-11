#!/usr/bin/python
from pytube import YouTube, Playlist
from utils.common import get_video_resolution_choice, get_output_path, get_audio_playlist
from utils.message import video_resolution_messages
def select_video_resolution(url, video_playlist):
    print(video_resolution_messages['intro_message'])

    try:
        if video_playlist:
            playlist = Playlist(url)
            youtube = YouTube(url)
            video_stream = youtube.streams.filter(adaptive=True, file_extension="webm").order_by('resolution').desc()
            # audio_stream = youtube.streams.filter(only_audio=True).order_by('abr').desc()
            user_choice = get_video_resolution_choice(video_stream)
            # chosen_audio_stream = audio_stream[1]  # static audio quality 128kbps for all videos
            # chosen_video_stream = video_stream[user_choice - 1]
            playlist_list = []  # Initialize a list to store video streams
            for video_url in playlist.video_urls:
                video = YouTube(video_url)
                video_stream = video.streams.filter(adaptive=True, file_extension="webm").order_by('resolution').desc()[user_choice - 1]
                playlist_list.append(video_stream)
            audio_playlist, playlist = get_audio_playlist(url)

            return playlist_list, audio_playlist, get_output_path(playlist.title)  # Return the list of audio streams for the playlist and the path

        else:
            # video_resolution = int(input(video_resolution_messages['enter_resolution_number']))
            youtube = YouTube(url)
            video_stream = youtube.streams.filter(adaptive=True, file_extension="webm").order_by('resolution').desc()
            audio_stream = youtube.streams.filter(only_audio=True).order_by('abr').desc()
            user_choice = get_video_resolution_choice(video_stream)

            chosen_audio_stream = audio_stream[1]  # static audio quality 128kbps for all videos
            chosen_video_stream = video_stream[user_choice - 1]
            return chosen_video_stream, chosen_audio_stream, get_output_path(chosen_video_stream.title)


        #     print(video_resolution_messages['wrong_resolution_msg'])
    except Exception as e:
        print(video_resolution_messages['exception_msg'], str(e))
