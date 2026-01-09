import httpx
from aiofiles.os import access

login_payload = {
    "email": "test@test.com",
    "password": "test"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

login_header ={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=login_header)
me_response_data = me_response.json()

print(me_response_data)