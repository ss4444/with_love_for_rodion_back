from pydantic import BaseModel


class Predict(BaseModel):
    smiles: str
