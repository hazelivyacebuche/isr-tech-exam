from pydantic import BaseModel
from selenium.webdriver.common.action_chains import ActionChains

class Login(BaseModel):

    username: str
    password: str
    
class LoginPage:
    username = "input[name='uid']"
    password = "input[name='password']"
    submit_btn = "input[name='loginSubmit']"