from fastapi import APIRouter,UploadFile, File
import pymupdf
import easyocr

router = APIRouter()

reader = easyocr.Reader(['en'], gpu=False)

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    
    pdf_bytes = await file.read()
    text = ""

    with pymupdf.open(stream = pdf_bytes,filetype = "pdf") as pdf:
        for page in pdf :
            text += page.get_text()


    words = text.split()
    if not words:
        return []

    chunks = []
    chunk_size,overlap = 200,50
    step = chunk_size - overlap
    for start in range(0, len(words), step):
        chunk_words = words[start:start + chunk_size]
        chunks.append(" ".join(chunk_words))

        if start + chunk_size >= len(words):
            break  # reached the end of the text

    return {
            "Total": len(chunks),
            "Chunk" : chunks
    }


@router.post('/image')
async def image(image: UploadFile = File(...)):
    image_bytes = await image.read()
    text = reader.readtext(image_bytes, detail=0)
    return {"text": " ".join(text), "lines": text}