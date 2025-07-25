import yt_dlp

def download_video(url, output_path="downloads", audio_only=False):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'quiet': False,
        'noplaylist': True,
    }

    if audio_only:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best'
        })

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading from: {url}")
        ydl.download([url])

# 🧪 Test URLs (Replace with any public video URL)
#    ydl_opts.update -> 'merge_output_format': 'mp4'
video_url = 'https://www.youtube.com/watch?v=izbydia9jz4'  # Example YouTube URL
download_video(video_url, output_path='D:\\Media\\Video', audio_only=False)