from pydantic import BaseModel, Field
from typing import Literal

class GraphStatus(BaseModel): 
    status: Literal["FINISH", "CONTINUE"] = Field(description= "Finish if the input of user was answered with success, continue if needs to rerun the graph to generate a new anser.")