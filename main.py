from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}



cities = {
    1: {"id": 1, "name": "New York", "country": "USA"},
    2: {"id": 2, "name": "London", "country": "UK"},
    3: {"id": 3, "name": "Tokyo", "country": "Japan"},
}

@app.get("/cities/{id}")
def read_city(id: int):
    return {"id": id, "city": cities.get(id, "City not found")}

@app.get("/cities")
def read_cities():
    return {"cities": list(cities.values())}