import requests

print(requests.get("http://0.0.0.0:8000/employees/10").json())
print(requests.get("http://0.0.0.0:8000/employees/9").json())

response = requests.post(
    "http://0.0.0.0:8000/employees",
    json={
        "name": "Thien",
        "department": "IT",
        "salary": 80000,
        "hire_date": "2026-01-10"
    }
)

print(response.status_code)
print(response.json())