import os
import sys
import yt_dlp

def download_video(video_id, output_path):
    try:
        yt_url = f'https://www.youtube.com/watch?v={video_id}'

        ydl_opts = {
            'format': 'bestvideo[height<=2160]+bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
        print(f"Downloaded video in 4K or highest available resolution: {yt_url}")
    except Exception as e:
        print(f"Error downloading video {video_id}: {e}")

def download_playlist(playlist_id, output_path):
    try:
        playlist_url = f'https://www.youtube.com/playlist?list={playlist_id}'

        ydl_opts = {
            'format': 'bestvideo[height<=2160]+bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(playlist)s/%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print(f"Downloaded playlist in 4K or highest available resolution: {playlist_url}")
    except Exception as e:
        print(f"Error downloading playlist {playlist_id}: {e}")

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
