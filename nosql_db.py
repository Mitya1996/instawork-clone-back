# Google's free firestore database (if you don't use it too much)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


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
