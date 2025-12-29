import requests 

URL:str = "http://127.0.0.1:5000"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

response = requests.get(
    url=URL + "/",
    headers = headers
)
print("Risposta GET:", response.json())

response = requests.get(
    url=URL + "/devices",
    headers = headers
)
print("Risposta GET:", response.json())


payload = {
    "type": "laptop",
    "id": "L002",
    "model": "MacBook Pro 16",
    "customer_name": "Giulia Verdi",
    "purchase_year": 2023,
    "status": "received",  
    "has_dedicated_gpu": True,
    "screen_size_inches": 16
}

response_post = requests.post(
    url=URL + "/devices",  
    json=payload,
    headers=headers
)

print("Risposta POST:", response_post.json())

response = requests.get(
    url=URL + "/devices/L002",
    headers = headers
)
print("Risposta GET:", response.json())

payload = {
    "status": "repairing"
}

response_patch = requests.patch(
    url=URL + "/devices/L002/status",
    json=payload,
    headers=headers
)

print("Risposta PATCH:",response_patch.json())


payload = {
    "type": "laptop",
    "id": "L002",  
    "model": "MacBook Pro 16 M2",
    "customer_name": "Giulia Verdi",
    "purchase_year": 2024,
    "status": "in_repair",
    "has_dedicated_gpu": True,
    "screen_size_inches": 16
}



response_put = requests.put(
    url=URL + "/devices/L002",
    json=payload,
    headers=headers
)

print("Risposta PUT:", response_put.json())


response_delete = requests.delete(
    url=URL + "/devices/L002",
    headers=headers
)

print("Risposta DELETE:",response_delete.json())

response_get = requests.get(
    url=URL +"/devices/L002",
    headers=headers
)

print("Risposta GET:",response_get.json())