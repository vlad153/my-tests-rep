from fastapi import FastAPI
from .config import config


app = FastAPI()


@app.get("/")
def check_install():
    data = {
        "project_name": config.PROJECT_NAME,
        "first_superadmin_email": config.FIRST_SUPERADMIN_EMAIL,
        "first_superadmin_password": config.FIRST_SUPERADMIN_PASSWORD,
    }
    return data
