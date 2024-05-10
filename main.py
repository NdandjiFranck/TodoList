from fastapi import FastAPI

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata

#import router
import routers.router_todos
import routers.router_auth

app = FastAPI(
    title="To do List",
    description=api_description,
    openapi_tags= tags_metadata
)

app.include_router(routers.router_todos.router)
app.include_router(routers.router_auth.router)

