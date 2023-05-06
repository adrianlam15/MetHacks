import openai
import os
from dotenv import load_dotenv
from pdfHelper import extract_text

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

TEXT = extract_text("./backend/sample_inputs/solar_system_questions.pdf")
flashcards = []


# COMMENTED OUT TO AVOID USING API CREDITS
# response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt="Generate flash cards given this text, and minimize token usage:\n\n" + text,
#     temperature=0,
#     max_tokens=200,
#     top_p=1,
#     frequency_penalty=0.5,
#     presence_penalty=0,
# )
# generated_text = response.choices[0]["text"]


# TEST CASE
response = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": "null",
            "text": "Flash Cards:\nQ1: What is the smallest planet in our Solar System?\nA1: Mercury\n\nQ2: How long does it take for light to reach the Earth from the Sun?\nA2: 8 minutes and 20 seconds.\n\nQ3: What is the largest moon in the Solar System?\nA3: Ganymede.\n\nQ4: What is the only planet in our Solar System known to have active plate tectonics?\nA4: Earth. \n\nQ5: What is the hottest planet in our Solar System? \nA5: Venus. \n\nQ6: What is the most abundant gas in Earth's atmosphere? \nA6: Nitrogen.",
        }
    ],
    "created": 1683338309,
    "id": "cmpl-7D1TpQJFKrB3Ez9JcCMx6LMGDMB9r",
    "model": "text-davinci-003",
    "object": "text_completion",
    "usage": {"completion_tokens": 153, "prompt_tokens": 108, "total_tokens": 261},
}
generated_text = response["choices"][0]["text"]


for line in generated_text.split("\n"):
    if line.startswith("Q"):
        question_num = line[:2]
        question = line[4:]
    elif line.startswith("A"):
        answer_num = line[:2]
        answer = line[4:]
        flashcards.append({question_num: question, answer_num: answer})

print(flashcards[0])
print(flashcards[0]["Q1"])
print(flashcards[0]["A1"])
