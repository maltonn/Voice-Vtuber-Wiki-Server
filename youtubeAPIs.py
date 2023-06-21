from apiclient.discovery import build

with open('keys/youtube-api-key.txt') as f:
    YOUTUBE_API_KEY = f.read().strip()

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def GetChannelInfo(channelId,is_user_channel=False):
    if is_user_channel:
        channel_response = youtube.search().list(
            part = "snippet",
            type="channel", # 検索対象をチャンネルのみに限定
            q=channelId, # 検索クエリ
        ).execute()
        channelId=channel_response["items"][0]["id"]["channelId"]
    else:
        channel_response = youtube.channels().list(
            part='snippet',
            id=f'{channelId},'
        ).execute()
        
    channelSnippetInfo = channel_response["items"][0]["snippet"]
    # {
    #     'title': '藍月なくる / Aitsuki Nakuru',
    #     'description': '藍月なくるです。\nリアルとバーチャルを行き来するシンガー。クラゲが好き。\n歌ってみたやオリジナル楽曲のＭＶ、ＣＤを作....',
    #     'customUrl': '@aitsukinakuru',
    #     'publishedAt': '2017-06-07T12:01:10Z',
    #     'thumbnails': {
    #         'default': {'url': 'https://yt3.ggpht.com/sfirurbg89IYHmv5sMPYd5nHm8gxeb7YivXcvaZgdqe4NZHI1RcyL7G8sGK3zQaMi7VvuAnfEJo=s88-c-k-c0x00ffffff-no-nd-rj', 'width': 88, 'height': 88},
    #         'medium': {'url': 'https://yt3.ggpht.com/sfirurbg89IYHmv5sMPYd5nHm8gxeb7YivXcvaZgdqe4NZHI1RcyL7G8sGK3zQaMi7VvuAnfEJo=s240-c-k-c0x00ffffff-no-nd-rj', 'width': 240, 'height': 240},
    #         'high': {'url': 'https://yt3.ggpht.com/sfirurbg89IYHmv5sMPYd5nHm8gxeb7YivXcvaZgdqe4NZHI1RcyL7G8sGK3zQaMi7VvuAnfEJo=s800-c-k-c0x00ffffff-no-nd-rj', 'width': 800, 'height': 800}
    #     },
    #     'localized': {'title': '藍月なくる / Aitsuki Nakuru', 'description': '藍月なくるです。\nリアルとバーチャルを行き来するシンガー。クラゲが好き。\n歌ってみたやオリジナル楽曲のＭＶ、ＣＤを作ったり音楽活動をしてます。\n最近はTRPGの配信にもお邪魔したり。\n\n■御依頼・お問い合わせ\nホームページのコ ンタクトからどうぞ！\nhttps://aitsukinakuru.com/\n\n■Twitter\nhttps://twitter.com/NakuruAitsuki\n■Ci-en\nhttps://ci-en.net/creator/7588\n\n■ファンレター送り先\n〒151-0071\n東京都渋谷区本町1丁目40ｰ14\u3000カームコート初台306\u3000\n株式会社 一二三\n'},
    #     'country': 'JP'
    # }
    return {
        "channel_id": channelId,
        "channel_title": channelSnippetInfo["title"],
        "channel_thumbnail": channelSnippetInfo["thumbnails"]["medium"]["url"],
        "channel_description": channelSnippetInfo["description"] if "description" in channelSnippetInfo else ""
    }


def GetChannelFromVideo(videoId):
    videos_response = youtube.videos().list(
        part='snippet,statistics',
        id=f'{videoId},'
    ).execute()
    # snippet
    VideosnippetInfo = videos_response["items"][0]["snippet"]
    # VideosnippetInfo={
    #     'publishedAt': '2022-02-02T12:00:10Z',
    #     'channelId': 'UCQHCHIoeu0FRJTJNMG2_Ezw',
    #     'title': 'フォニイ / covered by 藍月なくる',
    #     'description': 'Original：フォニイ / phony - kafu [オリジナル]\nhttps://youtu.be/9QLT1Aw_45s\n\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈\n\n◆Credit（敬称略）\n\nVocal：藍月なくる\nTwitter：https://twitter.com/NakuruAitsuki\nHP：http://qulalimstella.com/\n\nMix：Meis Clauson\nhttps://twitter.com/meisclauson\n\nIllustration：BORUMETE\nhttps://twitter.com/BORUMETE\n\nMovie：らいり\nhttps://twitter.com/_Rai28\n\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈',
    #     'thumbnails': {
    #         'default': {'url': 'https://i.ytimg.com/vi/Nv1dsznzMKw/default.jpg','width': 120,'height': 90},
    #         'medium':{'url': 'https://i.ytimg.com/vi/Nv1dsznzMKw/mqdefault.jpg','width': 320, 'height': 180},
    #         'high': {'url': 'https://i.ytimg.com/vi/Nv1dsznzMKw/hqdefault.jpg', 'width': 480, 'height': 360},
    #         'standard': {'url': 'https://i.ytimg.com/vi/Nv1dsznzMKw/sddefault.jpg', 'width': 640, 'height': 480}
    #         },
    #     'channelTitle': '藍月なくる / Aitsuki Nakuru',
    #     'categoryId': '10',
    #     'liveBroadcastContent': 'none',
    #     'localized': {'title': 'フォニイ / covered by 藍月なくる', 'description': 'Original：フォニイ / phony - kafu [オリジナル]\nhttps://youtu.be/9QLT1Aw_45s\n\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈\n\n◆Credit（敬称略）\n\nVocal：藍月なくる\nTwitter：https://twitter.com/NakuruAitsuki\nHP：http://qulalimstella.com/\n\nMix：Meis Clauson\nhttps://twitter.com/meisclauson\n\nIllustration：BORUMETE\nhttps://twitter.com/BORUMETE\n\nMovie：らいり\nhttps://twitter.com/_Rai28\n\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈'},
    #     'defaultAudioLanguage': 'en'
    # }

    channel_id = VideosnippetInfo['channelId']
    return channel_id

def GetGoodVideoFromChannel(channelId):#雑談と名の付く動画を取得
    request = youtube.search().list(
        part="snippet",
        channelId=channelId,
        maxResults=3,  # You can adjust this value
        type="video",
        q="雑談"
    )
    response = request.execute()

    for item in response['items']:
        print(item['snippet']['title'])
        if '雑談' in item['snippet']['title']:
            return item['id']['videoId'], item['snippet']['title']

    return None,None


def GetVideoTitle(vodeoId):
    videos_response = youtube.videos().list(
        part='snippet,statistics',
        id=f'{vodeoId},'
    ).execute()
    # snippet
    VideosnippetInfo = videos_response["items"][0]["snippet"]
    return VideosnippetInfo["title"]

