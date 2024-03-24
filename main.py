from fastapi import FastAPI

#from branch.api import BranchAPI
from result.api import ResultAPI
# from user.api import UserAPI


app = FastAPI()

# app.include_router(UserAPI.router)
app.include_router(ResultAPI.router)

#app.include_router(Branch.router)
