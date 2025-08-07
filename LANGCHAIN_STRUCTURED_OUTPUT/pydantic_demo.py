from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str ='Shailesh' #default value of name is Shailesh
    age : Optional[int]=None #default value of age is Nonve
    email : EmailStr
    cgpa  : float =Field(gt=0,lt=10,default=5, description= 'decimal value represting the cgpa of the student')
    
new_student= {'age':'32','email':'abc@gmail.com'} # pydantic is internally coercing the data type from str to int 

student=Student(**new_student)
print("Pydantic Student ",student)
print("Pydantic Student type ",type(student))
student_dict=dict(student)
print(student_dict['age'])

json=student.model_dump_json()
print("Student in json format ",json)