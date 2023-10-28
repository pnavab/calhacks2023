import reflex as rx

import os
import requests


def root():
    return {"test"}

def get_ai_response():
  url = 'https://api.together.xyz/inference'
  headers = {
      'Authorization': 'Bearer ' + "0293565af33ec96cf7ccd0b83ef5ff381d673d58781ad5ee0a7841dcf0a66504",
      'accept': 'application/json',
      'content-type': 'application/json'
  }

  data = {
      "model": "togethercomputer/RedPajama-INCITE-7B-Instruct",
      "prompt": "The capital of France is",
      "max_tokens": 128,
      "stop": ".",
      "temperature": 0.7,
      "top_p": 0.7,
      "top_k": 50,
      "repetition_penalty": 1
  }

  response = requests.post(url, json=data, headers=headers)
  response_json = response.json()
  print(response.json())
  answer = response_json['output']['choices'][0]['text']
  answer = answer.strip()
  return answer