import os
import sys
import time
import yt_dlp

def log(message):
    print(f"[youtube-archiver] {message}")

def download_content(url, output_path, retries=3, wait_time=60, custom_template=None):
    for attempt in range(retries):
        try:
            ydl_opts = {
                'format': 'bestvideo[height<=2160]+bestaudio/best',
                'outtmpl': os.path.join(output_path, custom_template if custom_template else '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'ignoreerrors': True,
                'concurrent_fragment_downloads': os.cpu_count(),
                'postprocessors': [
                    {
                        'key': 'EmbedThumbnail',
                        'already_have_thumbnail': False
                    },
                    {
                        'key': 'FFmpegMetadata',
                        'add_chapters': True,
                        'add_infojson': 'if_exists',
                        'add_metadata': True
                    }
                ],
                'writethumbnail': True
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            log(f"Downloaded content: {url}")
            break
        except Exception as e:
            log(f"Error downloading content from {url}: {e}")
            if attempt < retries - 1:
                log(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)

def archive_youtube(id_type, id_value, output_path):
    if id_type == 'video':
        yt_url = f'https://www.youtube.com/watch?v={id_value}'
        download_content(yt_url, output_path)
    elif id_type == 'playlist':
        playlist_url = f'https://www.youtube.com/playlist?list={id_value}'
        download_content(playlist_url, output_path, custom_template='%(playlist)s/%(title)s.%(ext)s')
    elif id_type == 'channel':
        channel_url = f'https://www.youtube.com/c/{id_value}'
        download_content(channel_url, output_path, custom_template='%(uploader)s/%(title)s.%(ext)s')
    else:
        log("Invalid ID type. Use 'video', 'playlist', or 'channel'.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        log("Usage: python youtube_archiver.py [video|playlist|channel] <ID> <output_path>")
        sys.exit(1)

    id_type = sys.argv[1]
    id_value = sys.argv[2]
    output_path = sys.argv[3]

    archive_youtube(id_type, id_value, output_path)
