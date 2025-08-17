# 🤖 AI-Powered Code Explainer

An **AI-powered tool** that explains code snippets using **Groq API** and **OpenRouter API**.  
You can paste your code into the input block, then choose which AI engine (Groq or OpenRouter) to generate explanations.

---

## 🚀 Features
- ✍️ Paste any code snippet directly into the input block.
- 🔄 Select between **Groq API** and **OpenRouter API** for explanations.
- 📘 Get clear, AI-powered explanations of your code.
- 🌐 Lightweight and simple web-based interface.

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask/FastAPI)  
- **APIs Used:**  
  - [Groq API](https://groq.com/)  
  - [OpenRouter API](https://openrouter.ai/)  

---

## 📂 Project Structure

- Ai-Powered-Code-Explainer/
- │── app.py # Backend logic (Flask/FastAPI server)
- │── background.js # Handles extension background tasks
- │── popup.html # UI for code input
- │── popup.js # Handles frontend logic and API calls
- │── styles.css # Styling for popup
- │── README.md # Project documentation

---

## ⚡ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nikhil-tej108/Ai-Powered-Code-Explainer-.git
   cd Ai-Powered-Code-Explainer-
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Set up API keys**

      Create a .env file in the root directory and add:
      ```bash
      GROQ_API_KEY=your_groq_api_key_here
      OPENROUTER_API_KEY=your_openrouter_api_key_here
 4. ** Run the app**
     ```bash
        python app.py

  or, if this is used as a browser extension, load it into Chrome/Edge:

Open chrome://extensions/

Enable Developer mode

Click Load unpacked

Select the project folder  

🖥️ Usage

Paste your code snippet into the input block.

Click "Explain with Groq" or "Explain with OpenRouter".

Get instant AI-powered explanations!

📜 License

This project is licensed under the MIT License – feel free to use and modify it.
    

   


