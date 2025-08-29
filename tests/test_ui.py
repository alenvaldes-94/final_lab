import time
import requests

BASE = "http://localhost:8000"

def wait_up(url, timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code < 500:
                return
        except Exception:
            pass
        time.sleep(1)
    raise AssertionError("error, la app no inicio")

def test_health():
    wait_up(f"{BASE}/health")
    r = requests.get(f"{BASE}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_homepage():
    wait_up(f"{BASE}/health")
    r = requests.get(f"{BASE}/")
    assert r.status_code == 200
    assert "Hola mundo CI/CD" in r.text
