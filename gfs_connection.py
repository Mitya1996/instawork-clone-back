# Google's free firestore database (if you don't use it too much)

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


# firebase_admin.initialize_app(cred(), {
#     'projectId': 'instawork-clone',
# })

# db = firestore.client()


# if there is a /gcp path then
import os
gcp = os.path.isfile('/gcp')

if gcp:

    # Use a service account (gcp hosted)
    cred = credentials.Certificate('gcp/service-account-key.json')
    firebase_admin.initialize_app(cred)

else:
    # Use the application default credentials (local development)
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': 'instawork-clone',
    })

db = firestore.client()
