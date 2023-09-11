# import os
from _2_select_category import select_category
from _3_select_video_resolution import select_video_resolution
from _5_select_download import select_video_download, select_audio_download, select_audio_playlist_download, select_video_playlist_download
from _4_select_audio_quality import select_audio_quality


class MasterDownloader:
    @staticmethod
    def start():
        # return the url from select_category function
        url, video_flag, audio_flag, video_playlist, audio_playlist = select_category()
        # print("audio_playlist", audio_playlist)

        if url and video_flag:
            video_resolution_result = select_video_resolution(url, video_playlist)
            print("video_resolution_result", video_resolution_result)
            if video_resolution_result is not None:
                chosen_video_stream, chosen_audio_stream, path = video_resolution_result
                # if chosen_video_stream and path:
                if chosen_video_stream and chosen_audio_stream and path:
                    if video_playlist:
                        # select_video_playlist_download(chosen_video_stream, None, path)
                        select_video_playlist_download(chosen_video_stream, chosen_audio_stream, path)
                    else:
                        select_video_download(chosen_video_stream, chosen_audio_stream, path)
                else:
                    pass
            else:
                pass

        elif url and audio_flag:
            audio_quality_result = select_audio_quality(url, audio_playlist)
            if audio_quality_result is not None:
                chosen_audio_stream, path = audio_quality_result
                if chosen_audio_stream and path:
                    if audio_playlist:
                        select_audio_playlist_download(chosen_audio_stream, path)
                    else:
                        select_audio_download(chosen_audio_stream, path)
            else:
                print("Failed to retrieve audio quality information.")


if __name__ == "__main__":
    downloader = MasterDownloader()
    downloader.start()



