# PromptMuleClient Demo Application

PromptMuleClient is a Python demo application designed to interact with the PromptMule API. It allows users to send prompts to PromptMule, a service that enhances application development through API caching.

## Features

- Send prompts to the PromptMule API.
- Retrieve and display responses in a formatted manner.
- Measure and display the latency for each API request.
- Indicate whether responses are retrieved from the cache, highlighting efficiency and cost savings.
- Display token usage information for each response.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.x.
- You have a basic understanding of Python programming.
- You have an API key from PromptMule.

## Installation

To install PromptMuleClient, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/promptmuleclient.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd promptmuleclient
   ```

## Usage

To use PromptMuleClient, you need to initialize the client with your API key and then use the `send_prompt` method to send prompts to the PromptMule API. Here is a simple example:

```python
from promptmule_client import PromptMuleClient

api_key = "your_api_key_here"
prompt_mule_client = PromptMuleClient(api_key)

prompt = "Your prompt here."
response = prompt_mule_client.send_prompt(prompt)

print(response)
```

## Configuration

You can configure the following in the `PromptMuleClient` class:
- `api_key`: Your unique API key for accessing the PromptMule API.
- `max_tokens`: The maximum number of tokens to be used in the response (default is 100).

## Contributing

Contributions to the PromptMuleClient project are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your_feature`).
3. Make changes and commit (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your_feature`).
5. Open a pull request.

## License

MIT Licensed
---

For more information, please visit [PromptMule API Documentation](https://api.promptmule.com/docs).
