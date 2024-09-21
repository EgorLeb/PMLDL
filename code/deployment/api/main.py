from fastapi import FastAPI, HTTPException, status
from fastapi import File, UploadFile, Form
import numpy as np
import torch
import cv2
import model


app = FastAPI()

best_model = model.CNNClassificationModel()
ckpt = torch.load("best.pt", weights_only=True)
best_model.load_state_dict(ckpt)
best_model.eval()


def predict(file, predicting_model):
    arr = np.fromstring(file, 'uint8')
    im = cv2.imdecode(arr, cv2.COLOR_BGR2RGB)

    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    res = cv2.resize(im, dsize=(178, 218), interpolation=cv2.INTER_CUBIC)

    res_torch = np.array([res[..., 0], res[..., 1], res[..., 2]])
    res_torch = np.array(res_torch, dtype='f') / 255

    res_torch = torch.from_numpy(res_torch)
    p = float(predicting_model(res_torch.unsqueeze(0)))
    p = 1 if p >= 0 else 0
    return p


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.post("/upload")
def upload(filename: str = Form(...), file: UploadFile = File(...)):
    res = "Blond"
    try:
        contents = file.file.read()
        if predict(contents, best_model) == 0:
            res = "Not Blond"
    except Exception as e:
        print(e)
        return {"message": f"{e}"}
    finally:
        file.file.close()
    return {"message": f"{res}"}
