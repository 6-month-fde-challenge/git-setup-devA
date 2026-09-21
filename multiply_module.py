from input_variables import a , b
from secrets import api_key
from login import user_name,pass_word
from profile import profile_name

def multuply(a,b):
    if api_key:
        if profile_name == "veerandra":
            print("API key present and loggedin")
            return a*b


    