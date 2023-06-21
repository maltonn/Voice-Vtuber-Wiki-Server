from pyannote.audio import Model,Inference
import numpy as np

def GetEmbedding(path):
    with open ("keys/hf-token.txt") as f:
        hf_token=f.read().strip()
    model = Model.from_pretrained("pyannote/embedding",use_auth_token=hf_token)
    inference = Inference(model, window="whole")
    embedding = inference(path)
    return embedding

def ChoseBetstEmbed(embeddings):#複数のembeddingのうちのもっともよいもの＝他との類似度の合計が最も高いもの（？）
    embeddings/=np.linalg.norm(embeddings,axis=1,keepdims=True)
    simmus=np.dot(embeddings,embeddings.T)
    best_idx=np.argmax(np.sum(simmus,axis=1))

    return embeddings[best_idx]