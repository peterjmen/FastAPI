import matplotlib.pyplot as plt
from io import BytesIO
import base64
import requests

# Define the base URL of your FastAPI server
base_url = 'http://127.0.0.1:1987/'  # Change the port to match your FastAPI server

# Make a GET request to the root endpoint '/'
response_root = requests.get(f'{base_url}')
print("Response from root endpoint:")
print(response_root.json())

# Define the text to analyze
text_to_analyze = "This is a hardcoded variable being used, I am very happy"

# Make a GET request to the sentiment analysis endpoint
response_analyzed_sentiment = requests.get(f'{base_url}sentiment/{text_to_analyze}')
print("Sentiment to analyze:")
print(response_analyzed_sentiment.json())

# Make a GET request to the pie-chart endpoint
response_pie_chart = requests.get(f'{base_url}chart')
print("Response from pie-chart endpoint")
print("Commented out")

# # Decode and display the pie chart image
# html_content = response_pie_chart.text
# with open('pie_chart.html', 'w') as f:
#     f.write(html_content)

# You can optionally open 'pie_chart.html' in a web browser to view the pie chart.
