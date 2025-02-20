import json

import requests


def fetch_google_results(query):
    url = f"https://www.googleapis.com/customsearch/v1?key=AIzaSyCro-Ju0Q9BvLZCca7Ml0V4XiSWwYf7XQA&cx=46e66450d9d134b59&q={query}"

    response = requests.get(url)

    return response.json()


def write_results_to_file(results):
    with open("results.json", "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
