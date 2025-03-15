import requests

url = "http://127.0.0.1:5000/user/register"
data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword"
}

response = requests.post(url, json=data)
print(response.status_code)  # Should be 201 if successful
print(response.json())  # Prints the response JSON