from google import genai
count = 1
client = genai.Client(api_key="YourGeminiAPI")
lang = input("Enter Language: ")
while True:
    text = input("Enter Text: ")
    
    if text == "0":
        break
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Translate the following text to " + lang + ", or if its already " + lang + ", then translate it to English. Do NOT add any other words, it should be a copy-pastable text. Text: " + text
    )
    count += 1
    totest = response.text
    print(totest)
