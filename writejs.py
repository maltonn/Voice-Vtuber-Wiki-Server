import pickle
import numpy as np
import os
from db import AddData

def main():#独立して実行
    L=[]
    for i,filename in enumerate(os.listdir("pickles/")):
        # if i>20:
        #     break
                
        with open(f"pickles/{filename}", 'rb') as f:
            data=pickle.load(f)

            for key in [x for x in data.keys()]:
                if "channnel" in key:
                    key_correct=key.replace("channnel","channel")
                    data[key_correct]=data[key]
                    del data[key]
    
            with open(f"pickles/{filename}", 'wb') as f:
                pickle.dump(data,f)
                

        
        id=filename.split('.')[0]
        data["id"]=id
        data["embedding"]=(np.array(data["embedding"])*10000).astype(np.int64).tolist()
        L.append(data)
        print(data["channel_title"],data["video_title"])

        
        AddData(id,data)

    with open("../client/src/static.js", 'w',encoding="utf-8") as f:
        f.write(f"const static_lst={str(L)};export default static_lst")
    
    print("done writing static.js")
if __name__ == "__main__":
    main()