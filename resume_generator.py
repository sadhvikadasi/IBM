import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_resume(data):
    prompt = f"""
    Generate a professional, ATS-friendly resume for the following student data:
    Name: {data['name']}
    Email: {data['email']}
    Phone: {data['phone']}
    Education: {data['education']}
    Skills: {data['skills']}
    Projects: {data['projects']}
    Internships: {data['internships']}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

resume_text = generate_resume(user_data)
print(resume_text)