from fastapi import APIRouter, UploadFile, HTTPException, Depends
from app.services.html_converter import convert_file_to_html
from app.services.ai_assistants import AsistenteConversor
from app.services.file_handler import validate_file

router = APIRouter()

@router.post("/convert")
async def convert_file(file: UploadFile):
    try:
        file_type = validate_file(file)
    except HTTPException as e:
        raise e
        
    texto_extraido = convert_file_to_html(file)
    conversor = AsistenteConversor()
    html_from_assistant = await conversor.convertir(texto_extraido)  # Usa await

    return {
        "message": "La conversión fue exitosa",
        "result": {
            "file": file.filename,
            "convert_from_assistant_ia": html_from_assistant,            
        },
    }
