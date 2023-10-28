import reflex as rx

import os
import requests
import together

together.api_key="0293565af33ec96cf7ccd0b83ef5ff381d673d58781ad5ee0a7841dcf0a66504"

def root():
    return {"test"}

def get_ai_response(context: list, prompt):
  context_string = "\n".join([f"[INST] {item['user']} [/INST] {item['model']}" for item in context])
  print(f"{context_string} [INST] {prompt}")

  response_json = together.Complete.create(
     model= "togethercomputer/llama-2-7b-chat",
     prompt= f"Continue the story based on the following, but finish your answer somewhere the user can continue from: \n{context_string} [INST] {prompt} [/INST]",
     stop=["[INST]", "</s>"],
  )

  answer = response_json['output']['choices'][0]['text']
  answer = answer.strip()
  print(answer)
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