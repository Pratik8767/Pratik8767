from fastapi import FastAPI
from branch.branch_api import BranchAPI
from user.user_api import UserAPI

app=FastAPI()
#app.include_router(UserAPI.router)
app.include_router(BranchAPI.router)
