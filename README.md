# YouTube Archiver

A Python tool to archive YouTube videos and playlists by downloading them in the best available quality, including up to 4K resolution. This tool uses `yt-dlp` for downloading and outputs files in `.mp4` format for easy compatibility.

## Features

- Download YouTube videos in the highest available quality (up to 4K).
- Download entire YouTube playlists.
- Download all videos from a YouTube channel.
- Outputs files in `.mp4` format for easy compatibility.
- **Automatic retry** on download failures due to bot detection or temporary issues.

## Requirements

Before running the project, ensure you have the following installed:

- **Python 3.x**: You can download it from [Python.org](https://www.python.org/).
- **Dependencies**: Install via `pip` using the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```
- **FFmpeg**: Required for handling media files. Download and set up FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html).

### Installing FFmpeg on Windows

- Download FFmpeg from [FFmpeg Windows builds](https://ffmpeg.org/download.html#build-windows).
- Extract the contents and add the `bin` folder to your system's PATH environment variable.

Alternatively, you can install it using **Chocolatey** (if installed):

```bash
choco install ffmpeg
```

On **macOS**, you can install FFmpeg using **Homebrew**:

```bash
brew install ffmpeg
```

## Usage

Run the script with the following format:

```bash
python youtube_archiver.py [-h] [-c BROWSER] {video,playlist,channel} ID DEST
```

### Positional Arguments
- **{video,playlist,channel}**: The type of content to download.
- **ID**: The ID of the video, playlist or channel.
- **DEST**: The directory where the downloaded videos will be saved.

### Options

- **-h, --help**: Show the help message and exit.
- **-c BROWSER, --cookies BROWSER**: The browser to use for importing cookies. Supported browsers: `brave`, `chrome`, `chromium`, `edge`, `firefox`, `opera`, `safari`, `vivaldi`, `whale`. This enables features like access to age-restricted content.

## Troubleshooting

### No Sound in Windows Media Player

If you don't hear any sound while playing the video in **Windows Media Player**, it may be due to incompatibility with certain codecs used in the downloaded video file.

To fix this, use a different media player like **VLC**:

- Download **VLC Media Player** from [VLC's official website](https://www.videolan.org/vlc/).
- VLC is known for handling a wide variety of audio and video formats, and it should resolve the sound issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This tool uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) for downloading YouTube content.
- **FFmpeg** is used for handling media files.
