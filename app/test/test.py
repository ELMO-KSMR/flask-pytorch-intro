import requests

resp = requests.post(
    "http://localhost:5000/predict",
    files={"file": open("frog_32_thumb.png", "rb")},
)

print(resp.text)
