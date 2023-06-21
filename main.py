from youtubeAPIs import GetChannelInfo,GetChannelFromVideo,GetGoodVideoFromChannel,GetVideoTitle
from youtubeLibs import YTDownload,GetUrlType
from Triming import Triming
from RemoveBGM import RemoveBGM
from GetEmbedding import GetEmbedding,ChoseBetstEmbed
from db import AddData

import pickle

import numpy as np

import os

def main(url,save_pickle=False,save_firestore=False):
    
    os.makedirs("wavs/",exist_ok=True)
    os.makedirs("wavs/download/",exist_ok=True)
    os.makedirs("wavs/trim/",exist_ok=True)
    os.makedirs("wavs/only-voice/",exist_ok=True)

    video_id=None
    url_type,id=GetUrlType(url)
    if url_type=="Video":
        video_id=id
        channel_id=GetChannelFromVideo(id)
        channel_info=GetChannelInfo(channel_id)
        video_title=GetVideoTitle(video_id)
    elif url_type=="Channel":
        channel_id=id
        channel_info=GetChannelInfo(id)
        video_id,video_title=GetGoodVideoFromChannel(id)
    elif url_type=="UserChannel":
        channel_info=GetChannelInfo(id,is_user_channel=True)
        channel_id=channel_info.channel_id
        video_id,video_title=GetGoodVideoFromChannel(channel_info["channel_id"])
    else:
        return {'msg': 'invalid url'}, 400
    
    if not video_id:
        if save_pickle:
            with open("no-video-log.txt", 'a',encoding="utf-8") as f:
                tmp=channel_info["channel_title"]
                f.write(f"{tmp},{url}\n")

        return {'msg': 'no good video found'}, 400
        
    output=channel_info
    output['video_id']=video_id
    output['video_title']=video_title
    #  {
    #     "video_id": ,
    #     "video_title":,
    #     "channel_id": ,
    #     "channel_title",
    #     "channel_thumbnail": ,
    # }

    
    path=YTDownload(video_id)
    if not path:
        return {'msg': 'unable to download from youtube'}, 500

    print(path)
    path_lst=Triming(path,sample_num=3,duration=30) #sample_num箇所切り抜く
    if not path_lst:
        return {'msg': 'movie length too short'}, 400
    
    embeddings=[]
    for path in path_lst:
        path_only_voice=RemoveBGM(path,"wavs/only-voice/")
        emb=GetEmbedding(path_only_voice).tolist() #list (10,)
        embeddings.append(emb)
    res=ChoseBetstEmbed(np.array(embeddings)).tolist() #list (256,)


    output['embedding']=res
    if save_pickle:
        os.makedirs("pickles/",exist_ok=True)
        with open(f"pickles/{channel_id}.pkl", 'wb') as f:
            pickle.dump(output, f)

    if save_firestore:
        AddData(channel_id,output)


    return output, 200

