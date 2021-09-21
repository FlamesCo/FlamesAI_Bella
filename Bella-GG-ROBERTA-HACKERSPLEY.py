###!!!!!!!!! TEST 0.1##
import requests 
print("Hello, <3 I am your hacker girl Bella. Enjoy ho ho ho.")
API_URL = input("Enter api key")
print("Continue..API USER", API_URL)
headers = {"Authorization": "Bearer api_sUELMXKqdOCuyNWcNJnfOxiodbzBNLYMjE"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({"inputs": "Scanning all known exploits of hardware devices and software in the known history of the internet."})
print("You may now exit)")