import os
import time
import openai

class PoeticAssistant:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)
        self.system_message = "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."

    def compose_poem(self, topic):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": f"Compose a poem that explains the concept of {topic} in programming."}
                ]
            )
            return completion.choices[0].message['content']
        except openai.APIError as e:
            if e.status_code == 429:
                print("Rate limit exceeded. Waiting for 60 seconds before retrying.")
                time.sleep(60)
                return self.compose_poem(topic)
            else:
                raise

if __name__ == "__main__":
    assistant = PoeticAssistant(api_key=os.environ.get("OPENAI_API_KEY"))
    print(assistant.compose_poem("recursion"))
