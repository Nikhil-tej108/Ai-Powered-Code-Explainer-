from flask import Flask, render_template_string, request, jsonify
import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# API Keys
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

# API Configuration
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

def check_api_availability():
    """Check which APIs are configured"""
    return {
        'groq_available': bool(GROQ_API_KEY),
        'openrouter_available': bool(OPENROUTER_API_KEY)
    }

def explain_code_with_groq(code):
    """Explain code using Groq API"""
    if not GROQ_API_KEY:
        return {"success": False, "error": "Groq API key not configured"}

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a code explainer. Explain the given code clearly and concisely, including what it does, how it works, and any important details."},
            {"role": "user", "content": f"Please explain this code:\n\n{code}"}
        ],
        "max_tokens": 1000,
        "temperature": 0.1
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        explanation = data['choices'][0]['message']['content']
        return {"success": True, "explanation": explanation}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"API request failed: {str(e)}"}
    except KeyError as e:
        return {"success": False, "error": f"Unexpected API response format: {str(e)}"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {str(e)}"}

def explain_code_with_openrouter(code):
    if not OPENROUTER_API_KEY:
        return {"success": False, "error": "OpenRouter API key not configured"}

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/llama-3-70b-instruct",
        "messages": [
            {"role": "system", "content": "You are a code explainer. Explain the code clearly."},
            {"role": "user", "content": f"Explain the following code:\n\n{code}"}
        ],
        "max_tokens": 1000,
        "temperature": 0.1
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        explanation = data['choices'][0]['message']['content']
        return {"success": True, "explanation": explanation}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"API request failed: {str(e)}"}
    except KeyError as e:
        return {"success": False, "error": f"Unexpected API response format: {str(e)}"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {str(e)}"}

@app.route('/')
def index():
    with open('templates/index.html', 'r') as f:
        html_content = f.read()
    return html_content

@app.route('/status')
def status():
    api_status = check_api_availability()
    print(f"API Status: {api_status}")
    return jsonify(api_status)

@app.route('/explain', methods=['POST'])
def explain():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "No data provided"})

        code = data.get('code', '').strip()
        api_type = data.get('api', '').lower()

        if not code:
            return jsonify({"success": False, "error": "No code provided"})

        print(f"Explaining code with {api_type} API")
        print(f"Code snippet: {code[:100]}...")

        if api_type == 'groq':
            result = explain_code_with_groq(code)
        elif api_type == 'openrouter':
            result = explain_code_with_openrouter(code)
        else:
            return jsonify({"success": False, "error": "Invalid API type"})

        print(f"Result: {result.get('success', False)}")
        return jsonify(result)

    except Exception as e:
        print(f"Error in explain endpoint: {str(e)}")
        return jsonify({"success": False, "error": f"Server error: {str(e)}"})

if __name__ == '__main__':
    print("="*50)
    print("🚀 FAST CODE EXPLAINER STARTING")
    print("="*50)

    if GROQ_API_KEY:
        print("✅ Groq API configured")
    else:
        print("❌ Groq API not configured")
        print("   Get free key at: https://console.groq.com")

    if OPENROUTER_API_KEY:
        print("✅ OpenRouter API configured")
    else:
        print("❌ OpenRouter API not configured")
        print("   Get API key at: https://openrouter.ai")

    if not GROQ_API_KEY and not OPENROUTER_API_KEY:
        print("🔥 RECOMMENDATION: Get a free Groq API key or OpenRouter key!")
        print("   Visit: https://console.groq.com or https://openrouter.ai")

    print("="*50)
    app.run(debug=True, host='127.0.0.1', port=5000)
