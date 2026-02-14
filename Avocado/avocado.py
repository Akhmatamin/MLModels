from fastapi import APIRouter
from pydantic import BaseModel
import joblib


# scaler = joblib.load('scalerAvo.pkl')
model = joblib.load('Avocado/modelAvo2.pkl')

predict_router = APIRouter(prefix="/predict", tags=["predict"])


class Schema(BaseModel):
    firmness: float
    hue: int
    saturation: int
    brightness: int
    color_category: str
    sound_db: int
    weight_g: int
    size_cm3: int



@predict_router.post("/avo")
async def predict(schema: Schema):
    data = schema.dict()

    new_color = data.pop('color_category')
    color1234 = [
        1 if new_color == 'purple' else 0,
        1 if new_color == 'dark green' else 0,
        1 if new_color == 'green' else 0,
    ]

    features = list(data.values()) + color1234
    prediction = int(model.predict([features])[0])
    if prediction == 1:
        prediction = 'Hard'
    elif prediction == 2:
        prediction = 'Pre-conditioned'
    elif prediction == 3:
        prediction = 'Breaking'
    elif prediction == 4:
        prediction = 'Firm-ripe'
    else:
        prediction = 'Ripe'
    return {'Ripeness': prediction}



