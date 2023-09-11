from utils.message import video_category_messages

def select_category():
    # Initialize URLs and flags
    video_url, audio_url = None, None
    video_flag, audio_flag = False, False
    video_playlist, audio_playlist = False, False

    # The intro message and the category selection
    print(video_category_messages['intro_message'])
    print(video_category_messages['select_category'])

    try:
        select_cat = int(input(video_category_messages['select_vid_aud_number']))

        # The category section for video
        if select_cat == 1:
            print(video_category_messages['select_video_category'])
            video_category = int(input(video_category_messages['enter_video_cat_number']))
            if video_category == 1:
                video_url = input(video_category_messages['single_url'])
                video_flag = True
            elif video_category == 2:
                video_url = input(video_category_messages['playlist_url'])
                video_flag = True
                video_playlist = True
            else:
                print(video_category_messages['wrong_input'])
                return video_url, video_flag, audio_flag

        # The category section for audio
        elif select_cat == 2:
            print(video_category_messages['select_audio_category'])
            audio_category = int(input(video_category_messages['enter_audio_cat_number']))
            if audio_category == 1:  # single video url
                audio_url = input(video_category_messages['single_url'])
                audio_flag = True
            elif audio_category == 2:  # playlist video url
                audio_url = input(video_category_messages['playlist_url'])
                audio_flag = True
                audio_playlist = True
            else:
                print(video_category_messages['wrong_input'])
                return audio_url, audio_flag, video_flag
        else:
            print(video_category_messages['wrong_input'])
            return None

        # Return the selected URL and corresponding flags
        return (video_url, video_flag, audio_flag, video_playlist, audio_playlist) if video_url else (audio_url, video_flag, audio_flag, video_playlist, audio_playlist)

    # Exception handling
    except Exception as e:
        print(video_category_messages['exception_msg'], str(e))
