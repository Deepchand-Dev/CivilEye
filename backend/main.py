from fastapi import FastAPI, UploadFile, File , Form
from pathlib import Path
import shutil
app = FastAPI(title="CivicEye API")

UPLOAD_DIR = Path("../uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def home():
    return {"message": "CivicEye backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "path": str(file_path)
    }

@app.post("/complaints")
async def create_complaint(
    image: UploadFile = File(...),
    description: str = Form(...),
    location: str = Form(...)
):
    return {
        "message": "Complaint received",
        "description": description,
        "location": location
    }