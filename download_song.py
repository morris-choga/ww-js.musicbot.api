import urllib

from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC, TRCK, APIC
from mutagen.easyid3 import EasyID3
from pytube import YouTube
from moviepy.editor import *
import yt_dlp
import os

from pytube.exceptions import PytubeError


def download(title,video_id,location):
    link = f'https://music.youtube.com/watch?v={video_id}'
    # location = "C:\\Users\\Mchog\Desktop\\internship"



    # try:
    #
    #     yt = YouTube(link)
    #     yt.title = "".join([c for c in yt.title if c not in ['/', '\\', '|', '?', '*', ':', '>', '<', '"']])
    #     video = yt.streams.filter(only_audio=True).first()
    #     vid_file = video.download(output_path=location)
    #     base = os.path.splitext(vid_file)[0]
    #     audio_file = base + ".mp3"
    #
    # except Exception as e:
    #     print(f"Error has occured with ytmusicapi: {str(e)}")
    #     return f"Error has occured with ytmusicapi: {str(e)}"

    try:

        options = {
            'format': 'm4a/bestaudio/best',  # Choose the best available formats
            '--user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
            '--cookies':'/root/Downloads/cooffkies.txt',
            '--proxy':'198.176.56.44:80',
            'keepvideo': False,
            'cachedir': False,
            'outtmpl': f'{location}/%(title)s.%(ext)s',  # Output filename template
            # "ffmpeg_location": "C:\\Users\\Mchog\\Downloads\\ffmpeg-2024-02-15-git-a2cfd6062c-full_build\\bin",
            # "ffmpeg_location": "/usr/bin/ffmpeg",
            # 'postprocessors': [{
            #     'key': 'FFmpegExtractAudio',
            #     'preferredcodec': 'mp3',
            #     'preferredquality': '192',  # Preferred audio quality (kbps)
            # }],
        }



        with yt_dlp.YoutubeDL(options) as ydl:
            # result = ydl.download([link], cookies='/root/Downloads/cooffkies.txt')
            result = ydl.download([link])
            info_dict = ydl.extract_info(link, download=False)
            vid_title = info_dict.get('title', None)
            # os.replace(f"{location}\\{vid_title}.mp3", location + "\\" + title + ".mp3")
            audio = location + "/" + title + ".mp3"
            return audio



    except Exception as e:
        print(f"Error has occured with ytmusicapi: {str(e)}")
        return f"Error has occured with ytmusicapi: {str(e)}"



    # try:
    #
    #     mp4_no_frame = AudioFileClip(vid_file)
    #     mp4_no_frame.write_audiofile(audio_file, logger=None)
    #     mp4_no_frame.close()
    #     os.remove(vid_file)
    #     os.replace(audio_file, location + "/" + yt.title + ".mp3")
    #     audio_file = location + "/" + yt.title + ".mp3"
    #     return audio_file
    #
    #
    # except PytubeError as e:
    #     print(f"An error occured with PytubeError: " + str(e))
    #     return f"An error occured with PytubeError: " + str(e)
    #
    # except Exception as e:
    #     print(f"Error has occured: {str(e)}")
    #     return f"Error has occured: {str(e)}"


def tagger(title, artist, album, thumbnail, location):

    try:
        thumbnail = thumbnail
        mp3file = EasyID3(location)
        mp3file["albumartist"] = album
        mp3file["artist"] = artist
        mp3file["album"] = album
        mp3file["title"] = title
        mp3file["website"] = 't.me/mchoga'
        mp3file["tracknumber"] = str(1)
        mp3file.save()

        audio = ID3(location)
        audio.save(v2_version=3)

        audio = ID3(location)
        with urllib.request.urlopen(thumbnail) as albumart:
            audio["APIC"] = APIC(
                encoding=3, mime="image/jpeg", type=3, desc="Cover", data=albumart.read()
            )
        audio.save(v2_version=3)

    except Exception as e:
        print(f"An error occurred: {e}")
