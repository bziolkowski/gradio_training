from gradio_client import Client

client = Client("http://127.0.0.1:7860")

result = client.predict("Czy dziś może być czwartek?", api_name="/respond_single")

print(result)