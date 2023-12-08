

# Function to format the dictionary based on inputs
def format_dict(deliverable, subject, content, format="Markdown"):
    userPrompt = f"Create a {deliverable} for high school teachers specializing in {subject}, focusing on the topic: '{content}'."
    userPrompt += " This deliverable should serve as a guide for designing engaging classroom experiences."
    outputFormat = f"Please format the response in {format}."
    data = {
        "model": "gpt-3.5-turbo-1106",
        "messages": [
            {"role": "system", "content": "You are the most advanced AI-based NLP engine acting as an expert on the user's prompt topic and as a prompt enhancer"},
            {"role": "system", "content": "You must take user's prompt and provide an improved prompt at the end of your answer."},
            {"role": "user", "content": userPrompt},
            {"role": "user", "content": outputFormat}
        ]
    }
    return data