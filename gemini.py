from google import genai

client = genai.Client(api_key="AIzaSyBUUaVyyOdTS25VtZf_vOM4O3TMINOv5ys")
response = client.models.generate_content(
    model="gemini-1.5-flash", contents=input("Enter prompt :")
)
print(response.text)
