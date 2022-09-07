from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId
import json

student_router = APIRouter()
koneksi = connection.local.student

ref = '{"Documentation":"/docs","Created":"https://github.com/Ryas-Yusenda"}'
ref_object = json.loads(ref)


@student_router.get('/')
async def root():
    return ref_object


# GET ALL STUDENT
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(koneksi.find())


# GET A STUDENT
@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(koneksi.find_one({"_id": ObjectId(studentId)}))


# CREATE A STUDENT
@student_router.post('/students')
async def create_students(student: Student):
    koneksi.insert_one(dict(student))
    return listOfStudentEntity(koneksi.find())


# UPDATE A STUDENT
@student_router.put('/students/{studentId}')
async def update_students(studentId, student: Student):
   # Find student and update iy with new student data
    koneksi.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)},
    )
    return studentEntity(koneksi.find_one({"_id": ObjectId(studentId)}))


# DELETE A STUDENT
@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
   # Find student delete it and also return the same student objcet
    koneksi.find_one_and_delete({"_id": ObjectId(studentId)})
