
import pydub
from pydub import AudioSegment

def Triming(path,sample_num=3,duration=30):
    
    wav_filename=path.split("/")[-1].split(".")[0]
    base_sound = AudioSegment.from_file(path, format="wav")  # 音声を読み込み
    length_seconds = base_sound.duration_seconds  # 長さを確認
    if length_seconds < (sample_num+1)*duration:
        return None
    
    L=[]
    for div in range(1,sample_num+1):
        offset=div*(length_seconds-duration)*1000//(sample_num+1)
        div_sound = base_sound[offset:offset+duration*1000]  
        div_sound.export(f"wavs/trim/{wav_filename}_{div}.wav", format="wav") 
        L.append(f"wavs/trim/{wav_filename}_{div}.wav")
    
    return L
    
    