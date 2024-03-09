import os
import time
import openai

class CryptoAssistant:
    def __init__(self, api_key):
        """
        Initialize the CryptoAssistant class with the OpenAI API key.

        Args:
        api_key (str): The API key for accessing the OpenAI API.
        """
        self.client = openai.OpenAI(api_key=api_key)
        self.system_message = "You are a crypto assistant, skilled in explaining complex cryptocurrency concepts."

    def explain_concept(self, concept):
        """
        Generate an explanation of a given cryptocurrency concept.

        Args:
        concept (str): The cryptocurrency concept to be explained.

        Returns:
        str: The generated explanation.
        """
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": f"Explain the concept of {concept} in cryptocurrency."}
                ]
            )
            return completion.choices[0].message['content']
        except openai.APIError as e:
            if e.status_code == 429:
                print("Rate limit exceeded. Waiting for 60 seconds before retrying.")
                time.sleep(60)
                return self.explain_concept(concept)
            else:
                raise

if __name__ == "__main__":
    assistant = CryptoAssistant(api_key=os.environ.get("OPENAI_API_KEY"))
    concept = input("Please enter a cryptocurrency concept: ")
    print(assistant.explain_concept(concept))
