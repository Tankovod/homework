# ------------- LESSON 11, EXERCISE 1 -------------------
# make table category and functions to work with it

from pydantic import BaseModel, Field
from csv import DictReader
import sqlite3

csv_path = 'categories11_1.csv'
db_path = 'bd11_1.sqlite3'

cx = sqlite3.connect(db_path)

cu = cx.cursor()
create_cat_sql = "CREATE TABLE IF NOT EXISTS category(ID INTEGER PRIMARY KEY NOT NULL, " \
                 "name VARCHAR(127) NOT NULL, is_published BOOLEAN)"
cu.execute(create_cat_sql)
cx.close()


class PydentCat(BaseModel):
    name: str = Field(..., min_length=3, max_length=60)
    is_published: bool

    @classmethod
    def from_csv(cls, pth: str):
        with open(pth, 'r', encoding='utf-8') as file:
            lst = list(DictReader(file))

            pd_models = [cls(**dct) for dct in lst]

            return pd_models

    @staticmethod
    def write_into_db(models: list) -> None:
        for model in models:
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            add_to_cat_sql = "INSERT INTO category(name, is_published) VALUES(?, ?)"
            cursor.execute(add_to_cat_sql, (model.name, model.is_published))
            connection.commit()
            connection.close()

    @classmethod
    def get_data_from_cat(cls):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        get_cat_sql = "SELECT name, is_published FROM category"
        pd_models = []
        for row in cursor.execute(get_cat_sql):
            dct = dict(zip(('name', 'is_published'), row))
            pd_models.append(cls(**dct))
        connection.close()
        return pd_models


objs = PydentCat.from_csv(csv_path)
# PydentCat.write_into_db(objs)
print(PydentCat.get_data_from_cat())

