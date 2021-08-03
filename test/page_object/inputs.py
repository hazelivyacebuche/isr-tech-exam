from pydantic import BaseModel
from typing import List
from page_object.login_page import Login, LoginPage

class User(BaseModel):
    login: Login

class Inputs(BaseModel):
    user: User