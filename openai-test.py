import os
import time
import openai

client = openai.OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"))

while True:
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
            ]
        )
        print(completion.choices[0].message)
        break
    except openai.APIError as e:
        if e.status_code == 429:
            print("Rate limit exceeded. Waiting for 60 seconds before retrying.")
            time.sleep(60)
        else:
            raise
