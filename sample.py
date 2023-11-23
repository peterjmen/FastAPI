import requests

# Define the base URL of your FastAPI server
base_url = 'https://peterjmen-apps.ts.r.appspot.com/'

# Make a GET request to the root endpoint '/'
response_root = requests.get(f'{base_url}/')
print("Response from root endpoint:")
print(response_root.json())

# Make a GET request to the '/random/' endpoint
response_random = requests.get(f'{base_url}/random/')
print("\nResponse from '/random/' endpoint:")
print(response_random.json())

# Make a GET request to the '/random/{limit}' endpoint with a specific limit value (e.g., 50)
response_random_limit = requests.get(f'{base_url}/random/50')
print("\nResponse from '/random/{limit}' endpoint:")
print(response_random_limit.json())

# Make a GET request to the '/shoes' endpoint
response_shoes = requests.get(f'{base_url}/shoes')
print("\nResponse from '/shoes' endpoint:")
print(response_shoes.json())
