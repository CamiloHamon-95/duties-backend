from fastapi import APIRouter
from fastapi import HTTPException

from config.database2 import collection

from schema.schemas import list_serial
from schema.schemas import indiviual_serial 

from models.duties import Duty

from bson.objectid import ObjectId

from datetime import datetime

router = APIRouter()

response_schema = {
    'status_code':500, 
    'detail':'', 
    'response':'null'
}

# Get all pending tasks
@router.get('/api/duties')
def get_duties():
    try:
        get_duties = collection.find()
        if get_duties:
            response_schema['status_code'] = 200
            response_schema['detail'] = 'All tasks retrieved Successfully'
            response_schema['response'] = list_serial(get_duties)
            return response_schema
        else:
            return HTTPException(status_code=404, detail=f'Data from Database could not be retrieved')
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Some error occured {e}')

@router.get('/api/duties/{id}')
def get_duty(id: str):
    try:
        object_id = ObjectId(id)

        response = collection.find_one(filter={'_id': object_id})
        if response:
            response_schema['status_code'] = 200
            response_schema['detail'] = 'Data from duty retrieved Successfully'
            response_schema['response'] = indiviual_serial(response)
            return response_schema
        else:
            return HTTPException(status_code=404, detail=f'Data from duty with id {id} does not exists in the Database')
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Some error occured {e}')

@router.post('/api/duties')
def post_duty(duty: Duty):
    try:
        duty.modified_at = int(datetime.timestamp(datetime.now()))
        duty.created_at = int(datetime.timestamp(datetime.now()))
        response = collection.insert_one(dict(duty))
        if response:
            response_schema['status_code'] = 201
            response_schema['detail'] = 'New duty added to database Successfully'
            response_schema['response'] = {'id':str(response.inserted_id)}
        else:
            return HTTPException(status_code=500, detail='New duty could not be created in the Database')
        return response_schema
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Some error occured {e}')

@router.put('/api/duties/{id}')
def put_duty(id: str, duty: Duty):
    try:
        object_id = ObjectId(id)
        doc_exists = collection.find_one({'_id': object_id})
        if doc_exists:
            duty.modified_at = int(datetime.timestamp(datetime.now()))
            doc_update = collection.update_one({'_id': object_id}, {'$set': dict(duty)})
            if doc_update:
                response_schema['status_code'] = 200
                response_schema['detail'] = 'Duty was modified Successfully'
                response_schema['response'] = {'id':str(id)}
                return response_schema
            else:
                return HTTPException(status_code=500, detail=f'Duty could not be modified in the database')
        else:
            return HTTPException(status_code=404, detail=f'Data from duty with id {id} does not exists in the Database')
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Some error occured {e}')

@router.delete('/api/duties/{id}')
def delete_duty(id: str):
    try:
        object_id = ObjectId(id)
        response = collection.find_one_and_delete({'_id': object_id})
        if response:
            response_schema['status_code'] = 200
            response_schema['detail'] = 'Duty was deleted Successfully'
            response_schema['response'] = indiviual_serial(response)
            return response_schema
        else:
            return HTTPException(status_code=404, detail=f'Data from duty with id {id} does not exists in the Database')
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Some error occured {e}')