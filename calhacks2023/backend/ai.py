import reflex as rx

import os
import requests
import together
import base64
import re

together.api_key="0293565af33ec96cf7ccd0b83ef5ff381d673d58781ad5ee0a7841dcf0a66504"

def root():
    return {"test"}

def get_ai_response(context: list, prompt):
  context_string = "\n".join([f"[INST] {item['user']} [/INST] {item['model']}" for item in context])

  response_json = together.Complete.create(
     model= "togethercomputer/llama-2-7b-chat",
     prompt= f"The following dialogue represents an infinite choose-your-own-adventure story. Answer from the perspective of a narrator in an adventurous way, and keep it exciting and risky. \n{context_string} [INST] {prompt} [/INST]",
     stop=["[INST]", "</s>", "What do you do?"],
  )

  answer = response_json['output']['choices'][0]['text']
  answer = answer.strip()
  return answer

# context = [
#     {"user": "the boy pulls out a sword", "model": "the wolf struck at the boy"},
#     {"user": "the boy dodges", "model": "the wolf's jaws snapped shut just missing the boy's head."}
# ]
# response = get_ai_response(context, "the boy dodges")

# context.append({"user": "the boy dodges", "model": response})
# response = get_ai_response(context, "the boy runs away")
# context.append({"user": "the boy runs away", "model": response})
# response = get_ai_response(context, "in a sudden turn of events, the boy knocks out the wolf")

def get_ai_image(prompt, art_style):
   padded_prompt = f"in a[n] {art_style} style, draw this scenario: '{prompt}'"
   response = together.Image.create(prompt=padded_prompt, model="stabilityai/stable-diffusion-xl-base-1.0", width=1024, height=512)
   image = response["output"]["choices"][0]
   output = image["image_base64"]
  #  print(f"output is {output}")
   return output

def get_sentiment_colors(prompt):
  response_json = together.Complete.create(
     model= "togethercomputer/llama-2-13b-chat",
     prompt= f"[INST] Generate and return ONLY 2 hex codes for light toned colors, not very dark colors. They should represent the overall mood and setting of the following scenario: '{prompt}' [/INST]",
     stop=["[INST]", "</s>"],
     max_tokens=200
  )

  answer = response_json['output']['choices'][0]['text']
  answer = answer.strip()
  print("answer is", answer)
  return answer

def get_hex_codes(prompt):
  response = get_sentiment_colors(prompt)
  pattern = r'#([A-Fa-f0-9]{6})'
  
    # Use re.findall to find all matching patterns in the output
  hex_codes = re.findall(pattern, response)
  if len(hex_codes) < 2:
    return ['000000', 'ffffff']
  return hex_codes
