import re
from pytube import YouTube, Playlist
import os
import pyfiglet
import colorama
from colorama import Fore, Style

colorama.init()

def generate_ascii_title(title):
    ascii_title = pyfiglet.figlet_format(title)
    border = '-' * 80
    print(Fore.GREEN + border)
    print(ascii_title)
    print(border)
    print(Style.RESET_ALL)


def sanitize_filename(filename):
    sanitized_filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return sanitized_filename


def download_audio(video, folder_name, counter=None):
    try:
        if video.streams.filter(only_audio=True):
            audio = video.streams.filter(only_audio=True).first()
            sanitized_title = sanitize_filename(video.title)
            audio_filename = f"{sanitized_title}.mp3"
            print(f"Downloading audio: {sanitized_title}")
            audio.download(output_path=folder_name, filename=audio_filename)
            print("Download completed.")
        else:
            print("Error: No audio stream available for this video.")
    except Exception as e:
        print(f"Error downloading audio: {video.watch_url}")
        print(str(e))


def download_video(video_url, quality='720p', folder_name='', file_format='mp4', counter=None):
    try:
        video = YouTube(video_url)

        if file_format == 'mp3':
            download_audio(video, folder_name, counter)
        else:
            streams = video.streams.filter(res=quality, file_extension=file_format)

            if streams:
                video_title = video.title
                if counter is not None:
                    video_title = f"{counter}-{video_title}"
                sanitized_title = sanitize_filename(video_title)
                video_filename = f"{sanitized_title}.{file_format}"
                print(f"Downloading video: {sanitized_title}")
                streams.first().download(output_path=folder_name, filename=video_filename)
                print("Download completed.")
    except Exception as e:
        print(f"Error downloading video: {video_url}")
        print(str(e))


def download_playlist(playlist_url, quality='720p', folder_name='', file_format='mp4', start_index=1, display_counter=False):
    try:
        playlist = Playlist(playlist_url)

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for counter, video_url in enumerate(playlist.video_urls, start=1):
            if counter >= start_index:
                if display_counter:
                    download_video(video_url, quality, folder_name, file_format, counter)
                else:
                    download_video(video_url, quality, folder_name, file_format)

    except Exception as e:
        print(f"Error downloading playlist: {playlist_url}")
        print(str(e))


def main():
    generate_ascii_title("YT DOWNLOADER")

    option = int(input("Enter the option (1 for playlist, 2 for single video): "))

    if option == 1:
        playlist_url = input("Enter the YouTube playlist URL: ")

        folder_name = input("Enter the download folder name: ")

        start_index = int(input("Enter the starting index (default: 1): ") or 1)

        quality = input("Enter the video quality (default: 720p): ") or '720p'

        file_format = input("Enter the file format (default: mp4): ") or 'mp4'

        display_counter = input("Display counter with video names? (y/n, default: n): ").lower() == 'y'

        download_playlist(playlist_url, folder_name=folder_name, start_index=start_index, quality=quality,
                          file_format=file_format, display_counter=display_counter)

    elif option == 2:
        video_url = input("Enter the YouTube video URL: ")

        folder_name = input("Enter the download folder name: ")

        quality = input("Enter the video quality (default: 720p): ") or '720p'

        file_format = input("Enter the file format (default: mp4): ") or 'mp4'

        download_video(video_url, folder_name=folder_name, quality=quality, file_format=file_format)

    else:
        print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
