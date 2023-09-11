from pytube import YouTube, Playlist
from utils.message import video_resolution_messages
from utils.common import get_output_path, get_audio_playlist, get_audio_single

def select_audio_quality(url, audio_playlist):
    print(video_resolution_messages['intro_message'])
    # print("audio_playlist", audio_playlist)

    try:
        # ************ block start ************
        # Extracting the playlist audio one by one
        if audio_playlist:
            playlist_list, playlist = get_audio_playlist(url)  # to get the complete audio playlist (playlist_list) and playlist object
            return playlist_list, get_output_path(playlist.title)  # Return the list of audio streams for the playlist and the path
        else:
            # for the single audio file
            audio_single_stream = get_audio_single(url)  # to get the single audio
            return audio_single_stream, get_output_path(audio_single_stream.title)  # Return the single audio stream and the path
        # ************ block end ************
    except ValueError as eh:
        print("Invalid input - Please enter a number: ", str(eh))
    except Exception as e:
        print("An error occurred:", str(e))


