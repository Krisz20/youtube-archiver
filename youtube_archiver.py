import os
import sys
import time
import yt_dlp

def download_video(video_id, output_path, retries=3, wait_time=60):
    yt_url = f'https://www.youtube.com/watch?v={video_id}'

    for attempt in range(retries):
        try:
            ydl_opts = {
                'format': 'bestvideo[height<=2160]+bestaudio/best',
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt_url])
            print(f"Downloaded video in 4K or highest available resolution: {yt_url}")
            break
        except Exception as e:
            print(f"Error downloading video {video_id}: {e}")
            if attempt < retries - 1:
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)

def download_playlist(playlist_id, output_path, retries=3, wait_time=60):
    playlist_url = f'https://www.youtube.com/playlist?list={playlist_id}'

    for attempt in range(retries):
        try:
            ydl_opts = {
                'format': 'bestvideo[height<=2160]+bestaudio/best',
                'outtmpl': os.path.join(output_path, '%(playlist)s/%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([playlist_url])
            print(f"Downloaded playlist in 4K or highest available resolution: {playlist_url}")
            break
        except Exception as e:
            print(f"Error downloading playlist {playlist_id}: {e}")
            if attempt < retries - 1:
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)

def archive_youtube(id_type, id_value, output_path):
    if id_type == 'video':
        download_video(id_value, output_path)
    elif id_type == 'playlist':
        download_playlist(id_value, output_path)
    else:
        print("Invalid ID type. Use 'video' or 'playlist'.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python youtube_archiver.py [video|playlist] <ID> <output_path>")
        sys.exit(1)

    id_type = sys.argv[1]
    id_value = sys.argv[2]
    output_path = sys.argv[3]

    archive_youtube(id_type, id_value, output_path)