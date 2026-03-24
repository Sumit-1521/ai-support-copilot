from google import genai

client = genai.Client(api_key="AIzaSyDTEpQFTXsTHBd_RZ9Pb63xy1NKYjNk5U0")

models = client.models.list()

for m in models:
    print(m.name)