import os
import time
import openai

class PoeticAssistant:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)
        self.system_message = "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."

    def compose_poem(self, topic):
        return self.compose_content(topic, "Compose a poem that explains the concept of {topic} in programming.")

    def compose_story(self, topic):
        return self.compose_content(topic, "Compose a short story that involves the concept of {topic} in programming.")

    def compose_content(self, topic, prompt):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": prompt.format(topic=topic)}
                ]
            )
            return completion.choices[0].message['content']
        except openai.APIError as e:
            if e.status_code == 429:
                print("Rate limit exceeded. Waiting for 60 seconds before retrying.")
                time.sleep(60)
                return self.compose_content(topic, prompt)
            else:
                raise

if __name__ == "__main__":
    assistant = PoeticAssistant(api_key=os.environ.get("OPENAI_API_KEY"))
    topic = input("Please enter a programming concept: ")
    content_type = input("What type of content would you like? (poem/story): ")
    if content_type.lower() == "poem":
        print(assistant.compose_poem(topic))
    elif content_type.lower() == "story":
        print(assistant.compose_story(topic))
    else:
        print("Invalid content type. Please enter either 'poem' or 'story'.")
