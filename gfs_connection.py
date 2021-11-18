# Google's free firestore database (if you don't use it too much)
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# def cred():
#     GOOGLE_APPLICATION_CREDENTIALS_FILENAME = 'key.json'
#     # set GOOGLE_APPLICATION_CREDENTIALS_TEXT in Cloud Run and cloudbuild.yaml to service acct key (from secret mgr)
#     GOOGLE_APPLICATION_CREDENTIALS_TEXT = os.environ.get(
#         'GOOGLE_APPLICATION_CREDENTIALS_TEXT')

#     # if in cloud run environment
#     if GOOGLE_APPLICATION_CREDENTIALS_TEXT:
#         file = open(GOOGLE_APPLICATION_CREDENTIALS_FILENAME, 'w')
#         file.write(GOOGLE_APPLICATION_CREDENTIALS_TEXT)
#         file.close()
#         return credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS_FILENAME)
#     # if doing local development/testing
#     return credentials.ApplicationDefault()


firebase_admin.initialize_app(credentials.Certificate('/gcp/key.json'), {
    'projectId': 'instawork-clone',
})

db = firestore.client()
