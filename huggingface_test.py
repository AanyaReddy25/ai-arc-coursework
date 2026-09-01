import os
from huggingface_hub import InferenceClient

# Read the API token from the environment
token = os.environ["HF_TOKEN"]

# Connect to Hugging Face
client = InferenceClient(
    provider="auto",
    api_key=token
)

# Send one prompt to the model
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "user",
            "content": "Explain what an AI agent is in simple terms."
        }
    ]
)

# Print the response
print(response.choices[0].message.content)