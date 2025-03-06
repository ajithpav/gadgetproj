# import requests

# url = "https://shorturl.at/onbGO"  # Your shortened URL

# try:
#     response = requests.get(url)  # Sending a GET request
#     if response.status_code == 200:  # Use .status_code instead of .status
#         try:
#             data = response.json()  # Try parsing as JSON
#             print("Data:", data)
#         except requests.exceptions.JSONDecodeError:
#             print("Response is not JSON. Raw data:", response.text)
#     else:
#         print("Failed to get data. Status Code:", response.status_code)
# except requests.exceptions.RequestException as e:
#     print("Error:", e)

import requests

# Define the API endpoint URL
url = "https://jsonplaceholder.typicode.com/posts/1"  # Example API

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to JSON format
    print("Fetched Data:", data)
else:
    print("Failed to fetch data. Status Code:", response.status_code)

