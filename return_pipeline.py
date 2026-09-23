def add_print(a, b):

    print(a + b)

def add_return(a, b):

    return a + b

add_print(5,3)
add_return(5,3)


def receive_prompt(prompt):
    return prompt

def generate_response(prompt):
    return f"Model says: {prompt}"

def clean_response(response):
    return response.replace("Model says: ", "").strip()

def format_for_storage(cleaned_data):
    return cleaned_data.upper()



prompt = receive_prompt("Hello AI, please summarize this text")
response = generate_response(prompt)
cleaned = clean_response(response)
storage_ready = format_for_storage(cleaned)

print("Prompt:", prompt)
print("Model Response:", response)
print("Cleaned Response:", cleaned)
print("Storage-Ready Response:", storage_ready)
