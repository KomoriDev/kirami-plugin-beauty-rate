from kirami import get_driver
from pydantic import BaseModel

class Config(BaseModel):
    api_key: str = ""
    secret_key: str = ""


config = Config.parse_obj(get_driver().config.dict())
API_KEY = config.api_key
SECRET_KEY = config.secret_key
