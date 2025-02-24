This repository contains two FastAPI projects that leverage Pydantic for data validation:

fastapi_project → A FastAPI application for managing users and orders.

ML_sample → A FastAPI-powered Machine Learning model for house price prediction.

Both projects demonstrate how Pydantic ensures structured data handling and validation.

Project Structure:

C:\Users\YourDocument\pydantic\
│── fastapi_project/          # Standard FastAPI API
│   ├── main.py               # API routes
│   ├── models.py             # Pydantic models
│   ├── database.py           # SQLAlchemy database setup
│   ├── auth.py               # Authentication logic (JWT)
│   ├── routers/              # API routes (users, orders)
│── ML_sample/                # Machine Learning FastAPI API
│   ├── main.py               # API with ML model integration
│   ├── train_model.py        # Script to train and save ML model
│   ├── house_price_model.pkl # Trained ML model
│   ├── model_features.pkl    # Feature names for validation

inside the notebook will be all the necessary setup