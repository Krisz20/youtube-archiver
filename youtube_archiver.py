import os
import sys
import time
import yt_dlp
import argparse

supported_browsers = ['brave', 'chrome', 'chromium', 'edge', 'firefox', 'opera', 'safari', 'vivaldi', 'whale']

def log(message):
    print(f"[youtube-archiver] {message}")

def download_content(url, output_path, retries=3, wait_time=60, custom_template=None, cookies=None):
    for attempt in range(retries):
        try:
            ydl_opts = {
                'format': 'bestvideo[height<=2160]+bestaudio/best',
                'outtmpl': os.path.join(output_path, custom_template if custom_template else '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'ignoreerrors': 'only_download',
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

            if cookies:
                ydl_opts['cookiesfrombrowser'] = (cookies, None, None, None)

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return_code = ydl.download([url])
            log(f"Downloaded content: {url}")
            return return_code
        except Exception as e:
            log(f"Error downloading content from {url}: {e}")
            if attempt < retries - 1:
                log(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
    return 1

def archive_youtube(id_type, id_value, output_path, cookies=None):
    if id_type == 'video':
        yt_url = f'https://www.youtube.com/watch?v={id_value}'
        download_content(yt_url, output_path, cookies=cookies)
    elif id_type == 'playlist':
        playlist_url = f'https://www.youtube.com/playlist?list={id_value}'
        download_content(playlist_url, output_path, custom_template='%(playlist)s/%(title)s.%(ext)s', cookies=cookies)
    elif id_type == 'channel':
        channel_urls = [
            f'https://www.youtube.com/c/{id_value}',
            f'https://www.youtube.com/channel/{id_value}',
            f'https://www.youtube.com/@{id_value}'
        ]
        
        for channel_url in channel_urls:
            return_code = download_content(channel_url, output_path, custom_template='%(uploader)s/%(title)s.%(ext)s', cookies=cookies)
            if return_code == 0:
                break
            else:
                log(f"Failed to download content from {channel_url}.")
    else:
        log("Invalid ID type. Use 'video', 'playlist', or 'channel'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A Python tool to download and archive YouTube videos and playlists in high quality.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-c", "--cookies", help="The name of the browser to use for cookies.", choices=supported_browsers)
    parser.add_argument("TYPE", help="The type of ID to download (video, playlist or channel).", choices=['video', 'playlist', 'channel'])
    parser.add_argument("ID", help="The ID of the video, playlist or channel to download.")
    parser.add_argument("DEST", help="The path to save the downloaded content.")
    args = parser.parse_args()

    archive_youtube(args.TYPE, args.ID, args.DEST, args.cookies)
