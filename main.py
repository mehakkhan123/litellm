from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    api_key = os.getenv("GEMINI_API_KEY")

    response = completion(
        model="gemini/gemini-2.0-flash",
        messages=[
            {
                "role":"user",
                "content":"Who is the founder of Pakistan?"
            }
        ],
    )

    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
