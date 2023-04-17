from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware
from PIL import Image
from io import BytesIO
from schemas import Predict
import aiofiles
import os
import uvicorn
import DECIMER

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file)).convert('RGB')
    return image


@app.post('/')
async def upload_file(file: UploadFile = File(...)):
    path = file.filename
    async with aiofiles.open(path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    predict = DECIMER.predict_SMILES(path)
    os.remove(path)
    return Predict(smiles=str(predict))

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
