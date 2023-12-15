import requests
import json
import time

class PromptMuleClient:
    def __init__(self, api_key):
        self.base_url = "https://api.promptmule.com"
        self.headers = {"x-api-key": f"{api_key}"}
        print(f"[INFO] PromptMuleClient initialized with base URL: {self.base_url}")

    def send_prompt(self, myprompt, max_tokens=100):
        print(f"\n[REQUEST] Sending prompt to PromptMule: '{myprompt}'")
        endpoint = f"{self.base_url}/prompt"
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": myprompt}],
            "max_tokens": max_tokens,
            "temperature": "0",
            "api": "openai",
            "semantic": "1.0",
            "sem_num": "1"
        }

        start_time = time.time()  # Start timing

        try:
            response = requests.post(endpoint, json=data, headers=self.headers)
            response.raise_for_status()
            latency = time.time() - start_time  # Calculate latency

            response_json = response.json()
            print("[RESPONSE] Full response from PromptMule (formatted):")
            print(json.dumps(response_json, indent=4))  # Neatly formatted JSON

            content = response_json['choices'][0]['message']['content'] if 'choices' in response_json and response_json['choices'] else None
            is_cached = response_json['choices'][0].get('is_cached', False)
            token_usage = response_json['usage']  # Get token usage information

            return response_json, content, is_cached, latency, token_usage
            
        except requests.RequestException as e:
            print(f"[ERROR] Error occurred while sending prompt: {e}")
            return None, None, False, time.time() - start_time, None

# Example usage
api_key = "6VDD3H6B4Y8Aftlnm7n069JvRIkaucmOIj1YyE69"
prompt_mule_client = PromptMuleClient(api_key)

prompt = "In spanish, explain how an API Cache-as-a-service enhances generative ai application development."
print(f"\n[TEST] Testing performance and efficiency with this prompt: '{prompt}'")

response, content, is_cached_status, latency, token_usage = prompt_mule_client.send_prompt(prompt)
print(f"\n[PERFORMANCE] Request Latency: {latency:.2f} seconds")

if content:
    print("\n[CONTENT] Response from PromptMule:", content)
else:
    print("[CONTENT] Failed to get content from the response.")

# Correctly use the is_cached_status in the final print statement
cache_message = "This response was retrieved from the cache, saving cost." if is_cached_status else "This response was generated anew."
print(f"\n[CACHE INFO] {cache_message}")

# Print token usage information
if token_usage:
    print(f"[TOKEN USAGE] Total tokens: {token_usage['total_tokens']}, Completion tokens: {token_usage['completion_tokens']}, Prompt tokens: {token_usage['prompt_tokens']}")
