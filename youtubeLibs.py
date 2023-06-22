#from __future__ import unicode_literals

import os
import subprocess
import re


def GetUrlType(url):#channel or UserChannel or Video or Other
    pattern_channel = re.compile(r'(https?://)?(www\.)?(youtube\.com/channel/)(.*)')
    pattern_user_channel = re.compile(r'(https?://)?(www\.)?(youtube\.com/@)(.*)')
    pattern_video = re.compile(r'(https?://)?(www\.)?(youtube\.com/watch\?v=)(.*)')
    pattern_short_video = re.compile(r'(https?://)?(youtu\.be/)(.*)')
    
    match_channel = pattern_channel.match(url)
    match_user_channel = pattern_user_channel.match(url)
    match_video = pattern_video.match(url)
    match_short_video = pattern_short_video.match(url)
    
    if match_channel:
        return "Channel", match_channel.group(4)
    elif match_user_channel:
        return "UserChannel", match_user_channel.group(4)
    elif match_video:
        return "Video", match_video.group(4).split('&')[0]  # `&`以降は他のパラメータなので無視
    elif match_short_video:
        return "Video", match_short_video.group(3)
    else:
        return "Other", None

def YTDownload(id):
    out_path=f'wavs/download/{id}.wav'
    if id==None:
        return None
    if os.path.exists(out_path):
        return out_path
    url=f'https://youtu.be/{id}'
    
    
    try:
        os.system(f'yt-dlp -x --audio-format wav -o "./wavs/download/%(id)s.%(ext)s" {url}')
        # os.rename(f'{id}.wav',f'wavs/{id}.wav')
        return out_path
    except:
        return None


if __name__ == "__main__":
    YTDownload("https://youtu.be/K4xLi8IF1FM")
    