from huggingface_hub import InferenceClient
import os

# Create client using token from environment
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)


def get_resume_feedback(resume_text: str):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional resume analyzer. Provide improvement suggestions."
                },
                {
                    "role": "user",
                    "content": f"Analyze this resume and give improvement suggestions:\n{resume_text}"
                }
            ],
            max_tokens=500,
            temperature=0.5
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
    
def get_skill_gap_analysis(resume_text: str, job_description: str):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a career coach. Analyze the resume against the job description and identify skill gaps."
                },
                {
                    "role": "user",
                    "content": f"Analyze this resume:\n{resume_text}\n\nAgainst this job description:\n{job_description}\n\nIdentify skill gaps and suggest how to address them."
                }
            ],
            max_tokens=500,
            temperature=0.5
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
