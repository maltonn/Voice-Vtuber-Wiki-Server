import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

try:
    cred = credentials.Certificate('keys/firebase-key.json')
except FileNotFoundError:
    raise FileNotFoundError('keys/firebase-key.jsonが見つかりませんでした。\n https://console.cloud.google.com/iam-admin/serviceaccounts から鍵を作成してjsonを保存してください。')


app = firebase_admin.initialize_app(cred)

db = firestore.client()

def AddData(docname, data):
    doc_ref = db.collection(u'vtubers').document(docname)
    doc_ref.set(data)
