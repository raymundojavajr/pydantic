from fastapi import FastAPI
from routers import users, orders, background_tasks

app = FastAPI()  # ✅ Ensure this line is present

app.include_router(users.router)
app.include_router(orders.router)
app.include_router(background_tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Pydantic App!"}
