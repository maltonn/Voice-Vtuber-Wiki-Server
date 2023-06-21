# 声から探せるVTuberWiki
Webサイト  
[https://maltonn.github.io/Voice-Vtuber-Wiki-Client](https://maltonn.github.io/Voice-Vtuber-Wiki-Client)


発表資料  
[https://docs.google.com/presentation/d/1Rh9pHLIxdV3W1nT8LkYYqQgmz2zgS2G9RpdKkscMDGU/edit?usp=sharing](https://docs.google.com/presentation/d/1Rh9pHLIxdV3W1nT8LkYYqQgmz2zgS2G9RpdKkscMDGU/edit?usp=sharing)

クライアント側のソースコード  
[https://github.com/maltonn/Voice-Vtuber-Wiki-Client](https://github.com/maltonn/Voice-Vtuber-Wiki-Client)

## 各ファイルの説明

#### app.py  
サーバーを立てる  

#### main.py  
中核。すべてのファイルを集めてURL→データへの変換を実装  

#### youtubeAPIs.py  
YouTube Data API を叩くためのもの　ID→チャンネル情報の変換など   

#### youtubeLibs.py  
YouTubeのURLからその音声をダウンロードしてくる　出力は wavs/download  

#### Triming.py  
長い音声を適当な位置でトリミングする　出力は wavs/trim   

#### RemoveBGM.py , rbhmLib/ ,models/removebgm.pth  
音声からBGMを消去する。出力は wavs/only-voice  
参照：[https://github.com/tsurumeso/vocal-remover](https://github.com/tsurumeso/vocal-remover)

#### GetEmbedding.py  
音声からspeaker-embeddingを導出する  
参照：[https://huggingface.co/pyannote/embedding](https://huggingface.co/pyannote/embedding)

#### db.py  
Firestoreに結果を格納する  

#### test.py  
開発者用：main.pyの動きを確認する  

#### writejs.py
picklesに格納された情報をFirestoreやクライアントのstatic.jsに落とし込む  
準備：このレポジトリとクライアントのレポジトリを同階層に置く

