from pydantic import BaseModel


class Model(BaseModel):
    @classmethod
    def validate_json(cls, data:str):
        return cls.model_validate_json(data,strict=True)

class MyModel(Model):
    a: int
    b: int

print(MyModel.validate_json('{"a": "1", "b": "2"}'))