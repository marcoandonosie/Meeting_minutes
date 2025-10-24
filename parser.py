from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def parse_meeting(transcript):
    try:
        # Load environment variables 
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        #read the prompt from file
        with open("prompt.txt", "r", encoding="utf-8") as f:
            input_prompt = f.read()

        # Define your five prompts clearly and separately
        prompts = {
            "context": f"""
            Prompt: {input_prompt}
            Transcript:
            {transcript}
            """
        }
        

            

        
        # Helper function for making GPT calls
        def call_gpt(prompt):
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Use GPT-4o-mini for speed/cost; switch to GPT-4o for top accuracy
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content.strip()

        

        # Run the model for the prompt and store results as four separate ones
        #result_text = call_gpt(prompts["context"])

        #TEST; comment out when running real thing 
        with open("real_transcript_gold.txt", "r", encoding="utf-8") as f:
            gold = f.read()
        result_text = gold
        

        # Remove "ChatGPT said:" prefix if it exists
        clean_text = result_text
        if clean_text.startswith("ChatGPT said:"):
            clean_text = clean_text[len("ChatGPT said:"):].strip()
            print("awooga21", clean_text[:50])
        # Split output by 'DELIMITER' and clean up whitespace
        raw_sections = clean_text.split("DELIMITER")
        print("awooga22", raw_sections[0][:50])
        sections = [part.strip() for part in raw_sections]
        print("awooga23", sections[0][:50])
        return sections

    except Exception as e:
        print(f"Error during meeting parsing: {e}")
        return []