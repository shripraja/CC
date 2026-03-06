import requests
import urllib.parse

search_query = "Bhayandar East"

encoded_query = urllib.parse.quote(search_query)
url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + encoded_query

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Title:", data.get("title"))
    print("Description:", data.get("extract"))
    print("Page URL:", data.get("content_urls", {}).get("desktop", {}).get("page"))
else:
    print("No result found.")