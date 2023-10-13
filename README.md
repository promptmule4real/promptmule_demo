# PromptMule API Demo Suite Walkthrough

Welcome to the PromptMule API Demo Suite! This README offers a comprehensive guide to understanding the registration process and diving deep into the power-packed functionalities of the PromptMule API.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Registration Walkthrough](#registration-walkthrough)
- [Overview of the Demo Suite](#overview-of-the-demo-suite)
- [Additional Resources](#additional-resources)

## Prerequisites

Start your journey by initializing the necessary libraries and endpoints:

```python
# Essential imports for the demo
import os
import requests
import json
import textwrap

# Setting up the API endpoints for easy reference
ENDPOINT = 'https://api.promptmule.com/'
REGISTRATION = 'signup'   # Endpoint for developer registration
LOGIN = 'login'           # Endpoint to obtain a Token
KEY_GEN = 'api-keys'      # Endpoint to generate an API Key
PROMPT = 'prompt'         # Main endpoint for prompt caching
LIST_API_KEYS = 'api-keys/'  # Endpoint to list all registered API keys and their app names
DELETE = 'profile/'       # Endpoint to delete a username - use with caution!
```

## Registration Walkthrough

### 1. Set Up Your Registration Data

Personalize the demo by inputting your details. Ensure validity for seamless operations:

```python
# Input your registration details here
your_new_username = "YOUR_NEW_USERNAME"
your_new_password = "YOUR_NEW_PASSWORD"
your_real_email = "YOUR_REAL_EMAIL"
your_new_appname = "YOUR_NEW_APPS_NAME"
```

### 2. Construct the Registration API Call

Next, organize the data for the registration API call and execute the request. For those accustomed to `curl`, here's the equivalent command:

```bash
curl -X POST "https://api.promptmule.com/signup" \
     -H "Content-Type: application/json" \
     -d '{"username": "YOUR_NEW_USERNAME", "password": "YOUR_NEW_PASSWORD", "email": "YOUR_REAL_EMAIL"}'
```

Make sure to replace the placeholders with your details.

### 3. Email Verification

Once registered, you'll receive an email from PromptMule. Verify your email by clicking the embedded link.

### 4. Token Generation

With your email verified, log into the platform and secure your unique API Token.

## Overview of the Demo Suite

**Introduction**: The PromptMule API Demo Suite equips you to enrich your interaction with the PromptMule API. Send prompts, evaluate responses, and gauge cache effectiveness.

### Features:

- **Authenticate**: Connect seamlessly with the API.
- **API Key Management**: Generate or retrieve your unique key.
- **Dispatch Prompts**: Relay diverse prompts with tailored response settings.
- **Monitor**: Opt for a verbose mode to view detailed logs.
- **Comprehensive Reports**: Avail insights on prompt behavior and cache efficiency.

### How to Use:

1. **Begin**: Activate the script.
2. **Enter Credentials**: Key in your username, password, and application name.
3. **Verbose Mode**: Choose between detailed logs or a concise output.
4. **Cost-saving Strategy**: Input your strategy for the test prompts.
5. **Analyze Reports**: Post operations, obtain:
    - In-depth prompt feedback.
    - A usage overview.
    - A cache savings summary.
6. **Optional Profile Deletion**: Exercise caution, irreversible once done.

## Additional Resources

For those who prefer hands-on interaction, the PromptMule API Demo Suite is accessible as a Google Colab notebook via GitHub. Engage directly [here](https://colab.research.google.com/github/promptmule4real/demo/blob/main/promptmule_api_key_gen_demo.ipynb).

---

**Happy Exploring with PromptMule!**
```

You can save the above content as `README.md` in your GitHub repository.
