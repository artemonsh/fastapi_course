import requests

token = "fake-super-secret-token"
cookie = "abcde"
r = requests.get(
    "http://localhost:8000/payments/",
    params={"limit": 1, "skip": 2},
    headers={"x-token": token},
    cookies={"super_cookie": cookie}
)

print(r.text)
