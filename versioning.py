import requests

response = requests.get("https://api.github.com/repos/N4GR/ZZZ-Box-Art-Generator/releases/latest")

print(response.json())