# AI Resume Analyzer 🚀

An intelligent system that analyzes resumes against job descriptions using Groq's LLM API.


## 🛠️ Setup Instructions

### 1. Get Your API Key
1. Sign up at [Groq Cloud](https://console.groq.com/home)
2. Create a new API key from the dashboard
3. Copy your key

### 2. Configure Environment
Create a `.env` file in the project root:

```bash
# .env
API_KEY=your_groq_api_key_here

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver