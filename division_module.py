from input_variables import a , b
from secrets import api_key
from login import user_name,pass_word
from profile import profile_name

def division(a,b):
    if api_key:
        if profile_name == "veerandra":
            print("API key present and logged in")
            return a/b