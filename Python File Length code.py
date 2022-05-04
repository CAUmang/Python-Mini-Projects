import os
from pymediainfo import MediaInfo

def get_track_len(file_path):
    media_info = MediaInfo.parse(file_path)
    for track in media_info.tracks:
        if track.track_type == "Video":
            return int(track.duration)
    return 0
    
length_millisec = sum(get_track_len(f) for f in os.listdir(r'folder_path'))
length_sec = length_millisec/1000
length_min = length_sec/60

print(str(length_sec) + ' seconds')
print(str(length_min) + ' minutes')




