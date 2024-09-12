import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "22906249"))
    API_HASH = os.getenv("API_HASH", "a8aa1616cda4920822ee4305908486d6")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6076006606:AAGGRuQpNvdphZOxnHpLneROPHJ6ppKco20")
    sudo = os.getenv("SUDO", "7104899484")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
