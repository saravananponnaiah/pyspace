import yt_dlp

def download_video(url, output_path="downloads", audio_only=False, browser='chrome'):
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
            'format': 'bestvideo[height<=720]+bestaudio/best',
            'merge_output_format': 'mp4'
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading from: {url}")
            ydl.download([url])
    except Exception as e:
        print(f"Download error: {e}")

# 🧪 Test URLs (Replace with any public video URL)
#    ydl_opts.update -> 'merge_output_format': 'mp4'
# video_url = 'https://www.youtube.com/watch?v=izbydia9jz4'  # Example YouTube URL
# urls = ['https://www.youtube.com/watch?v=uOmDEK9i1nI', 'https://www.youtube.com/watch?v=DInfmi-YIiw',
#         'https://www.youtube.com/watch?v=B56dXfsxA2k', 'https://www.youtube.com/watch?v=1seR_ckLXz4',
#         'https://www.youtube.com/watch?v=yG2MoXdFB34', 'https://www.youtube.com/watch?v=Nu2pLnm450o',
#         'https://www.youtube.com/watch?v=dvWdFMCC1-I', 'https://www.youtube.com/watch?v=B_Ffu0CPYJ4',
#         'https://www.youtube.com/watch?v=YKmTjVYMHTk', 'https://www.youtube.com/watch?v=Nz1iHi0fhzI',
#         'https://www.youtube.com/watch?v=qoq8B8ThgEM', 'https://www.youtube.com/watch?v=SZzMSxMF_xA']

# urls = ['https://www.youtube.com/watch?v=u_nDlTN0fQk', 'https://www.youtube.com/watch?v=A04WawrDblo',
#         'https://www.youtube.com/watch?v=LRHSq0tTLB0', 'https://www.youtube.com/watch?v=-40r98DTT6o',
#         'https://www.youtube.com/watch?v=atVof3pjT-I', 'https://www.youtube.com/watch?v=L8V3ylj4NUA',
#         'https://www.youtube.com/watch?v=dImiR3Sr8Wo', 'https://www.youtube.com/watch?v=ty6mMk9HRh0']

# urls = ['https://www.youtube.com/watch?v=uOmDEK9i1nI', 'https://www.youtube.com/watch?v=DInfmi-YIiw',
#          'https://www.youtube.com/watch?v=B56dXfsxA2k', 'https://www.youtube.com/watch?v=1seR_ckLXz4',
#          'https://www.youtube.com/watch?v=yG2MoXdFB34', 'https://www.youtube.com/watch?v=Nu2pLnm450o',
#          'https://www.youtube.com/watch?v=dvWdFMCC1-I', 'https://www.youtube.com/watch?v=B_Ffu0CPYJ4',
#          'https://www.youtube.com/watch?v=YKmTjVYMHTk', 'https://www.youtube.com/watch?v=Nz1iHi0fhzI',
#          'https://www.youtube.com/watch?v=qoq8B8ThgEM', 'https://www.youtube.com/watch?v=SZzMSxMF_xA']

# urls = ['https://www.youtube.com/watch?v=iVXF7hKuR7o', 'https://www.youtube.com/watch?v=iiS2iV2_TiM',
#         'https://www.youtube.com/watch?v=UpujKw9M4sg', 'https://www.youtube.com/watch?v=r5v6OV6tHS0',
#         'https://www.youtube.com/watch?v=rM0lub7u9PM', 'https://www.youtube.com/watch?v=NV1W_GYgp7c',
#         'https://www.youtube.com/watch?v=iP86tGd_LBo', 'https://www.youtube.com/watch?v=SAcpESN_Fk4',
#         'https://www.youtube.com/watch?v=K-Ts-NFR62o', 'https://www.youtube.com/watch?v=jRDCWQP7rjI',
#         'https://www.youtube.com/watch?v=Q-oqI8bDdpw', 'https://www.youtube.com/watch?v=WzkU-yxS-yY',
#         'https://www.youtube.com/watch?v=_tsW8MKr468', 'https://www.youtube.com/watch?v=YQ6ShcAU_dQ',
#         'https://www.youtube.com/watch?v=MqHdM1iwvwA', 'https://www.youtube.com/watch?v=nPrhOHl0IMk',
#         'https://www.youtube.com/watch?v=rp3_FhRnIRw', 'https://www.youtube.com/watch?v=l6-yvD53E3o']

# urls = ['https://www.youtube.com/watch?v=OCg6BWlAXSw', 'https://www.youtube.com/watch?v=2mDCVzruYzQ',
#         'https://www.youtube.com/watch?v=LPeZOE8ZIHI', 'https://www.youtube.com/watch?v=cFzAw52wR2E',
#         'https://www.youtube.com/watch?v=d0wsNOzzoN8']

urls = ['https://www.youtube.com/watch?v=nAmC7SoVLd8']

for url in urls:
    download_video(url, output_path='D:\\Media\\Video\\Langchain', audio_only=False, browser='edge')