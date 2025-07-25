from pytube import YouTube

url = input("Enter YouTube URL: ")
vid = YouTube(url=url, use_oauth=True, allow_oauth_cache=True)

video_download = vid.streams.get_highest_resolution()
audio_download = vid.streams.get_audio_only()

# entry = YouTube(url=url, use_oauth=True, allow_oauth_cache=True)
print(f"Title: {vid.title}")
print(f"Author: {vid.author}")

# print(f"\nVideo Found: {entry}")
# print(f"\nDownloading Video...")
# video_download.download(output_path="D:\\Media\\Video", filename=f"{entry}.mp4")
# print(f"\nDownloading Audio...")
# audio_download.download(output_path="D:\\Media\\Audio", filename=f"{entry}.mp3")
# print("\nDownload Complete")