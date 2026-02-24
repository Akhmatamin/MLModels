from fastapi import APIRouter
from pydantic import BaseModel
import joblib

model = joblib.load('Mushrooms/random_model.pkl')

mushroom_router = APIRouter(prefix="/mushrooms", tags=["Mushrooms"])


class MushroomSchema(BaseModel):
    cap_shape: str
    cap_surface: str
    cap_color: str
    bruises: str
    odor: str

    gill_attachment: str
    gill_spacing: str
    gill_size: str
    gill_color: str

    stalk_shape: str
    stalk_root: str
    stalk_surface_above_ring: str
    stalk_surface_below_ring: str
    stalk_color_above_ring: str
    stalk_color_below_ring: str

    veil_color: str

    ring_number: str
    ring_type: str

    spore_print_color: str
    population: str
    habitat: str

CAP_SHAPE = ("c", "f", "k", "s", "x")
CAP_SURFACE = ("c", "f", "k", "s", "x")
CAP_COLOR = ("c", "e", "g", "n", "p", "r", "u", "w", "y")
BRUISES = ("t",)
ODOR = ("c", "f", "l", "m", "n", "p", "s", "y")

GILL_ATTACHMENT = ("f",)
GILL_SPACING = ("w",)
GILL_SIZE = ("n",)
GILL_COLOR = ("e", "g", "h", "k", "n", "o", "p", "r", "u", "w", "y")

STALK_SHAPE = ("t",)
STALK_ROOT = ("c", "e", "r")

STALK_SURFACE_ABOVE_RING = ("k", "s", "y")
STALK_SURFACE_BELOW_RING = ("k", "s", "y")

STALK_COLOR_ABOVE_RING = ("c", "e", "g", "n", "o", "p", "w", "y")
STALK_COLOR_BELOW_RING = ("c", "e", "g", "n", "o", "p", "w", "y")

VEIL_COLOR = ("o", "w", "y")

RING_NUMBER = ("o", "t")
RING_TYPE = ("f", "l", "n", "p")

SPORE_PRINT_COLOR = ("h", "k", "n", "o", "r", "u", "w", "y")

POPULATION = ("c", "n", "s", "v", "y")
HABITAT = ("g", "l", "m", "p", "u", "w")


@mushroom_router.post('/')
async def predict_mush(schema: MushroomSchema):
    data = schema.dict()

    new_cap_shape = data.pop("cap_shape")
    cap_shape0_1 = [
        1 if new_cap_shape == i else 0 for i in CAP_SHAPE
    ]

    new_cap_surface = data.pop("cap_surface")
    cap_surface0_1 = [
        1 if new_cap_surface == i else 0 for i in CAP_SURFACE
    ]

    new_cap_color = data.pop("cap_color")
    cap_color0_1 = [
        1 if new_cap_color == i else 0 for i in CAP_COLOR
    ]

    new_bruises = data.pop("bruises")
    bruises0_1 = [
        1 if new_bruises == i else 0 for i in BRUISES
    ]

    new_odor = data.pop('odor')
    odor0_1 = [
        1 if new_odor == i else 0 for i in ODOR
    ]

    new_gill_attachment = data.pop('gill_attachment')
    gill_attachment0_1 = [
        1 if new_gill_attachment == i else 0 for i in GILL_ATTACHMENT
    ]

    new_gill_spacing = data.pop('gill_spacing')
    gill_spacing0_1 = [
        1 if new_gill_spacing == i else 0 for i in GILL_SPACING
    ]

    new_gill_size = data.pop('gill_size')
    gill_size0_1 = [
        1 if new_gill_size == i else 0 for i in GILL_SIZE
    ]

    new_gill_color = data.pop('gill_color')
    gill_color0_1 = [
        1 if new_gill_color == i else 0 for i in GILL_COLOR
    ]

    new_stalk_shape = data.pop('stalk_shape')
    stalk_shape0_1 = [
        1 if new_stalk_shape == i else 0 for i in STALK_SHAPE
    ]

    new_stalk_root = data.pop('stalk_root')
    stalk_root0_1 = [
        1 if new_stalk_root == i else 0 for i in STALK_ROOT
    ]

    new_stalk_surface_above_ring = data.pop('stalk_surface_above_ring')
    stalk_surface_above_ring0_1 = [
        1 if new_stalk_surface_above_ring == i else 0
        for i in STALK_SURFACE_ABOVE_RING
    ]

    new_stalk_surface_below_ring = data.pop('stalk_surface_below_ring')
    stalk_surface_below_ring0_1 = [
        1 if new_stalk_surface_below_ring == i else 0
        for i in STALK_SURFACE_BELOW_RING
    ]

    new_stalk_color_above_ring = data.pop('stalk_color_above_ring')
    stalk_color_above_ring0_1 = [
        1 if new_stalk_color_above_ring == i else 0
        for i in STALK_COLOR_ABOVE_RING
    ]

    new_stalk_color_below_ring = data.pop('stalk_color_below_ring')
    stalk_color_below_ring0_1 = [
        1 if new_stalk_color_below_ring == i else 0
        for i in STALK_COLOR_BELOW_RING
    ]

    new_veil_color = data.pop('veil_color')
    veil_color0_1 = [
        1 if new_veil_color == i else 0 for i in VEIL_COLOR
    ]

    new_ring_number = data.pop('ring_number')
    ring_number0_1 = [
        1 if new_ring_number == i else 0 for i in RING_NUMBER
    ]

    new_ring_type = data.pop('ring_type')
    ring_type0_1 = [
        1 if new_ring_type == i else 0 for i in RING_TYPE
    ]

    new_spore_print_color = data.pop('spore_print_color')
    spore_print_color0_1 = [
        1 if new_spore_print_color == i else 0
        for i in SPORE_PRINT_COLOR
    ]

    new_population = data.pop('population')
    population0_1 = [
        1 if new_population == i else 0 for i in POPULATION
    ]

    new_habitat = data.pop('habitat')
    habitat0_1 = [
        1 if new_habitat == i else 0 for i in HABITAT
    ]

    features = [list(data.values()) +cap_shape0_1 + cap_surface0_1 +
    cap_color0_1 +
    bruises0_1 +
    odor0_1 +

    gill_attachment0_1 +
    gill_spacing0_1 +
    gill_size0_1 +
    gill_color0_1 +

    stalk_shape0_1 +
    stalk_root0_1 +
    stalk_surface_above_ring0_1 +
    stalk_surface_below_ring0_1 +
    stalk_color_above_ring0_1 +
    stalk_color_below_ring0_1 +

    veil_color0_1 +

    ring_number0_1 +
    ring_type0_1 +

    spore_print_color0_1 +
    population0_1 +
    habitat0_1
]
    prediction = int(model.predict(features)[0])
    if prediction == 0:
        return {'Prediction': 'Eatable'}
    else:
        return {'Prediction': 'Poisoned'}



