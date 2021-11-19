# Instawork Clone Backend

This service is made with FastAPI and GCP : )

live production version  
https://instawork-clone-back-ltgvqmmasq-ez.a.run.app/

![](/README_img/1.png)
![](/README_img/2.png)
![](/README_img/3.png)
![](/README_img/4.png)

# Setup

* You will have to create a GCP project and a firestore database.  
* A service account key with all permissions is also required.
* Download the service account key .json file and upload one to GCP Secret Manager and one into the root of this repository (make sure to .gitignore it). [Your local development environment will also require $GOOGLE_APPLICATION_CREDENTIALS set to the service account key path](https://cloud.google.com/docs/authentication/getting-started).
* Deploy this repository easily via Cloud Run, reference the service account key and mount it under 'gcp/service-account-key.json'    
* Note: along the way, you may have to "enable APIs", set up billing, and do other basic GCP tasks.


`uvicorn main:app --reload` to start the server locally

Cloud Run provides a https endpoint when the server is live