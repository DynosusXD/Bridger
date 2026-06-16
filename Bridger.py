from google import genai
count = 1
client = genai.Client()
while True:
    text = input("Enter Text: ")
    if text == "0":
        break
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Translate the following text to Vietnamese, or if its already vietnamese, then translate it to English. Do NOT add any other words, it should be a copy-pastable text. Text: " + text
    )
    count += 1
    totest = response.text
    print(totest)