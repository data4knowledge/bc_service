from typing import List
from pydantic import BaseModel
from typing import List, Union

class BCModel(BaseModel):
  uri: str
  name: str
  based_on: str

class BC(BaseModel):
  uri: str
  name: str
  based_on: str
  bc_narrower: Union[None,List[BCModel]]  