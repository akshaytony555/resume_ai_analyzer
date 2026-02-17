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
