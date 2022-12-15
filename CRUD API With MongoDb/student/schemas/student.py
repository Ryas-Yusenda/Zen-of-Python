# conver mongodb to json

def studentEntity(db_item) -> dict:
    return{
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phone": db_item["student_phone"]
    }


def listOfStudentEntity(db_item_list) -> list:
    list_student = []

    for item in db_item_list:
        list_student.append(studentEntity(item))

    return list_student
