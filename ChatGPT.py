import openai

# Set up the OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Use the completion endpoint to interact with ChatGPT
response = openai.Completion.create(
  model="gpt-4.0-turbo",
  prompt="Translate the following English text to French: 'Hello, how are you?'",
  max_tokens=50
)

# Print the model's response
print(response.choices[0].text.strip())
