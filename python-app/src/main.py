from fastapi import FastAPI
import uvicorn
import os


app = FastAPI()


@app.get("/")
def read_root():
    gpt_name = os.getenv("NAME")
    open_ai_key = os.getenv("KEY")
    return {"OpenAI Key": open_ai_key, "OpenAI Name": gpt_name}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.getenv("PORT"))
