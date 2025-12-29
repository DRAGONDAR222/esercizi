import requests 

URL:str = "http://127.0.0.1:5000"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# response = requests.get(
#     url=URL + "/",
#     headers = headers
# )
# print("Risposta GET:", response.json())

# response = requests.get(
#     url=URL + "/animals",
#     headers = headers
# )
# print("Risposta GET:", response.json())

# response = requests.get(
#     url=URL + "/animals/d1",
#     headers = headers
# )
# print("Risposta GET:", response.json())

# response = requests.get(
#     url=URL + "/animals/d1/food",
#     headers = headers
# )
# print("Risposta GET:", response.json())

# response = requests.get(
#     url=URL + "/animals/d1/food/adoption",
#     headers = headers
# )
# print("Risposta GET:", response.json())

payload = {
    "type": "dog",
    "id": "d3",
    "name": "Rocky",
    "age_years": 4,
    "weight_kg": 18.2,
    "breed": "Golden Retriever",
    "is_trained": True
}

response_post = requests.post(
    url= URL + "/animals/add",  
    json=payload,
    headers=headers
)

# print("Risposta POST:", response_post.json())

response = requests.get(
    url=URL + "/animals/d3",
    headers = headers
)
# print("Risposta GET:", response.json())


# payload = {
#     "type": "cat",
#     "id": "c3",
#     "name": "Luna",
#     "age_years": 3,
#     "weight_kg": 4.5,
#     "indoor_only": True,
#     "favorite_toy": "topolino"
# }

# response_post = requests.post(
#     url= URL + "/animals/add",  
#     json=payload,
#     headers=headers
# )

# print("Risposta POST:", response_post.json())

# response = requests.get(
#     url=URL + "/animals/c3",
#     headers = headers
# )
# print("Risposta GET:", response.json())


payload = {
    "adopter_name": "Giulia Rossi"
}

response_post = requests.post(
    url= URL + "/animals/d3/adopt",  
    json=payload,
    headers=headers
)

# print("Risposta POST:", response_post.json())

response = requests.get(
    url=URL + "/animals/d3/adoption",
    headers = headers
)
print("Risposta GET:", response.json())

