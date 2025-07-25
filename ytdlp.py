# *******************************************************************
# https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#download-options
# https://www.pythoncentral.io/yt-dlp-download-youtube-videos/
# *******************************************************************
import yt_dlp

URLS = ['https://www.youtube.com/watch?v=2qCpY38ompo']

def longer_than_a_minute(info, *, incomplete):
    """Download only videos longer than a minute (or with unknown duration)"""
    duration = info.get('duration')
    if duration and duration < 60:
        return 'The video is too short'
    return None


ydl_opts = {
    'match_filter': longer_than_a_minute,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)