# Building Simpe API
Building a simple api utilizing FastAPI, Uvicorn, and Python

## Installations 
Make sure you have installed FastApi and Uvicorn. In this repo I utilize vscode becuase of the accessibility of Thundercloud. 

## Downloading and Run
Once you clone the repository proceed to the folder that the repo was saved in and type
`uvicorn main:app --reload` to run the server. 

On your webrowser type: `http://localhost:8000/api/v1/users`. There you'll see the database.

If you are not using Vscode and don't have access to Thundercloud to test this api, Fastapi provides a doc url
to test your api. Go to `http://localhost:8000/docs` to test and run the api's function. 
