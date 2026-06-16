import requests

BASE = "http://127.0.0.1:8000"

def run():
    user = {"username": "smoketest_py", "email": "smoke_py@example.com", "password": "smokepass"}
    r = requests.post(f"{BASE}/auth/register", json=user)
    print("REGISTER", r.status_code, r.text)

    t = requests.post(f"{BASE}/auth/token", data={"username": user["username"], "password": user["password"]})
    print("TOKEN", t.status_code, t.text)
    if t.ok:
        token = t.json().get("access_token")
        h = {"Authorization": f"Bearer {token}"}
        e = requests.get(f"{BASE}/expenses", headers=h)
        print("EXPENSES", e.status_code, e.text)

if __name__ == '__main__':
    run()
