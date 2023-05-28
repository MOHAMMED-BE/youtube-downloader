# YT Downloader

YT Downloader is a Python script that allows you to download YouTube videos and playlists.
It provides a simple command-line interface to choose between downloading a single video or an entire playlist.
The script uses the pytube library for handling YouTube video downloads.

# Features :


# -------------------------------------------
### Downloading Single Videos

To download a single YouTube video, follow these steps:

1. Run the script and select option 2 for downloading a single video.
2. Enter the YouTube video URL.
3. Enter the download folder name.
4. Optionally, specify the video quality (default: 720p).
5. Optionally, specify the file format (default: mp4).

The video will be downloaded to the specified folder with the chosen quality and file format.



# -------------------------------------------
### Downloading Playlists

To download a YouTube playlist, follow these steps:

1. Run the script and select option 1 for downloading a playlist.
2. Enter the YouTube playlist URL.
3. Enter the download folder name.
4. Optionally, specify the starting index for the videos (default: 1).
5. Optionally, specify the video quality (default: 720p).
6. Optionally, specify the file format (default: mp4).
7. Optionally, choose whether to display the video counter in the file names.

The script will download all the videos in the playlist, starting from the specified index, to the specified folder with the chosen quality and file format. If the counter is displayed, it will be included in the file names.



# -------------------------------------------
###     Notes

**Note -1 :** The playlist videos will be downloaded in the order they appear in the playlist.

**Note -2 :** You can download single video or all playlist videos as mp3 format.

**Note -3 :** If you choose another video quality you must write it like [ 1080p ] not like [ 1080 ].



# -------------------------------------------
###     Installation

1. Clone the repository:

    git clone ttps://github.com/MOHAMMED-BE/youtube-downloader.git

2. Install the required dependencies:

    pip install pytube colorama pyfiglet



# -------------------------------------------
###         Usage



1. Go to the downloaded folder and open it in CMD or VSCode:

2.  Run the following script:

    python app.py



# -------------------------------------------
###      Requirements


- Python 3.6 or above
- Python package manager | pip
- pytube library
- colorama library
- pyfiglet library
