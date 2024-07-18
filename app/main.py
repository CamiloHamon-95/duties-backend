from fastapi.middleware.cors import CORSMiddleware

from routes.route_duty import router

from fastapi import FastAPI

app = FastAPI()

origins = [
    'http://localhost:3000',
    'http://frontend-duties:3000',
    'https://frontend-duties:3000',
    'frontend-duties:3000',
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(router)

@app.get('/')
def welcome():
    return {'message': 'Welcome to FastAPI'}