import os
import json
from openai import OpenAI

API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)


class OpenAIHandler:
    def __init__(self, api_key=API_KEY, model="gpt-4-0125-preview"):
        self.model = model

    def check_candidate_match(self, persona, candidate):
        system= "テンプレ用文章"
        content= "ほげほげ"
        messages = [
            {"role": "system", "content": f'{{"さんぷる:{system}"}}'},
            {"role": "user",   "content": content},
        ]
        
        response = client.chat.completions.create(model=self.model, messages=messages, response_format={"type":"json_object"})
        return response.choices[0].message


