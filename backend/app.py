
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


from pathlib import Path
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:63342"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = PROJECT_DIR / "frontend"

app.mount(
    "/styles",
    StaticFiles(directory=FRONTEND_DIR / "styles"),
    name="styles"
)

app.mount(
    "/scripts",
    StaticFiles(directory=FRONTEND_DIR / "scripts"),
    name="scripts"
)

class TextData(BaseModel):
    text: str


@app.get("/")
def home():
    return FileResponse(PROJECT_DIR / "frontend" / "Home.html")


BASE_DIR = Path(__file__).resolve().parent

@app.get("/{item_id}")
def item(item_id: str):
    with open(BASE_DIR /"pi.txt", "r") as file:
        pi = file.read()
    pi = pi.replace("\n", "")
    pi = pi.replace(".", "")

    bnn = item_id
    #nbb =bnn[::-1]


    if bnn  in pi:
        index = pi.find(bnn)
        return f"exist starting on {index + 1}."
    else:
        return "not right now"


@app.post("/process-text")
def process(data: TextData):

    load_dotenv()
    email_address = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = "test"
    msg["From"] = email_address
    msg["To"] = email_address
    msg.set_content("Hello, \n Testiiing!!")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_address, password)
        smtp.send_message(msg)

    print(msg.get_content())


