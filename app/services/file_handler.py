import os
from fastapi import UploadFile, HTTPException

def save_file(file: UploadFile) -> str:
    directory = "tem_files"
    os.makedirs(directory, exist_ok=True)

    file_location = os.path.join(directory, file.filename)
    
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    return file_location

def validate_file(file: UploadFile) -> str:
    file_type = file.filename.split('.')[-1].lower()
    if file_type not in ['docx', 'pdf', 'xlsx']:
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Only DOCX, PDF, and XLSX are allowed.")
    return file_type