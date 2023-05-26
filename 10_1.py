# ------------- LESSON 10, EXERCISE 1 -------------------
# from csv file make Pydentic object and back
from csv import DictWriter, DictReader
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

src_ = "users10_1.csv"


class RegPydenticModel(BaseModel):
    id: int = Field(..., ge=1)
    name: str = Field(..., min_length=5, max_length=15)
    email: EmailStr
    password: str = Field(..., min_length=10, max_length=45)

    @classmethod
    def from_csv(cls, file: str):
        with open(file, 'r', encoding='utf-8') as file:
            lst = list(DictReader(file))

            pd_models = [cls(**dct) for dct in lst]

            return pd_models

    @classmethod
    def to_csv(cls, ob, file: str):
        lst = [dict(o) for o in ob]

        with open(file, 'w', encoding='utf-8') as file:
            r = DictWriter(file, fieldnames=lst[0].keys())
            r.writeheader()
            for dct in lst:
                r.writerow(dct)


obj = RegPydenticModel.from_csv(src_)
RegPydenticModel.to_csv(obj, src_)

