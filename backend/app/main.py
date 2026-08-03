from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "project": "RepoMind AI",
        "status": "Running",
        "version": "0.1.0"
    }