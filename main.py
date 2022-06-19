from fastapi import FastAPI
from model.system import SystemOut
from neo4j.neo4j_database import Neo4jDatabase
from neo4j.bc_instance import BCInstance
from fastapi_pagination import Page, add_pagination, paginate
from model.BC_output import BC


tags_metadata = [
    {
       "name": "System Info",
       "description": "Provides information of the version of the BC micro service version."
        },
    {
        "name": "BC List",
        "description": "The listing of all BCs in the data base.",
    },
    {
        "name": "Specific Instance of a BC",
        "description": "Returns the BC that in the name of the BC contains the string specified in the <b>name</b> parameter."
        }
    
]

VERSION = "0.1"
SYSTEM_NAME = "d4k BC Microservice"

app = FastAPI(
  title = SYSTEM_NAME,
  description = "A microservice to handle Biomedical Concepts in a Neo4j database.",
  version = VERSION
 # ,openapi_tags=tags_metadata
)

@app.get("/", 
  summary="Get system and version",
  description="Returns the microservice system details and the version running.", 
  response_model=SystemOut)
async def read_root():
  return SystemOut(**{ 'system_name': SYSTEM_NAME, 'version': VERSION })

@app.get("/biomedical_concepts/",
  summary="BC Listing",
  description="The listing of all BCs in the data base.", 
  response_model=Page[BC])
async def bc_list():
  return paginate(BCInstance.list_bcs())

@app.get("/biomedical_concepts/{name}",
  summary="BC Instance",
  description="Specific Instance of a BC.", 
  response_model=Page[BC])
async def bc_search(name: str):
 return paginate(BCInstance.find_bc(name))

add_pagination(app)
