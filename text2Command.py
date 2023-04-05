import os
import openai
from dotenv import load_dotenv

load_dotenv();

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Convert this text to a programmatic command: list all process the system is running by myself on linux terminal",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.2,
  presence_penalty=0
)
command = response.choices[0]["text"] if "choices" in response else "echo No response"
# execute the command that openai generated
os.system(command);