from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fetch_utils import fetch_google_results, write_results_to_file

app = FastAPI()

# Needed due to CORS restrictions
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def test(request_text):
    results = fetch_google_results(request_text)
    write_results_to_file(results)
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
