# 🎬 AI Movie Information Extractor

An AI-powered Streamlit application that extracts structured movie information from unstructured text using **LangChain**, **Mistral AI**, and **Pydantic**.

## 📌 Overview

Movie Information Extractor converts natural language movie descriptions into structured JSON data. Simply paste a movie paragraph, and the application identifies key details such as the title, release year, genre, director, cast, rating, and summary.

## ✨ Features

* 🎬 Extracts movie information from free-text descriptions
* 🤖 Powered by Mistral AI through LangChain
* 📄 Converts unstructured text into structured JSON
* ✅ Uses Pydantic for schema validation
* ⚡ Interactive Streamlit web interface
* 🔍 Displays both raw AI output and validated structured data

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Mistral AI
* Pydantic
* python-dotenv

## 📂 Project Structure

```text
Movie-Information-Extractor/
│
├── UIcore.py (or your Streamlit main file)
├── core.py
├── requirements.txt
├── .env
└── README.md
```

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/movie-information-extractor.git
cd movie-information-extractor
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create a `.env` file

```env
MISTRAL_API_KEY=your_api_key_here
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

Replace `app.py` with your Streamlit file name if it is different.

## 📥 Example Input

```
Inception is a science fiction film released in 2010. It was directed by Christopher Nolan and stars Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy, and Ken Watanabe. The movie has an IMDb rating of 8.8 and follows a skilled thief who enters people's dreams to plant an idea into someone's subconscious.
```

## 📤 Example Output

```json
{
  "title": "Inception",
  "release_year": 2010,
  "genre": [
    "Science Fiction"
  ],
  "director": "Christopher Nolan",
  "cast": [
    "Leonardo DiCaprio",
    "Joseph Gordon-Levitt",
    "Elliot Page",
    "Tom Hardy",
    "Ken Watanabe"
  ],
  "rating": 8.8,
  "summary": "A skilled thief enters dreams to plant an idea into someone's subconscious."
}
```

## 💡 Future Enhancements

* Support extraction of TV shows and web series
* Export extracted data to CSV or Excel
* Batch processing of multiple movie descriptions
* Genre classification improvements
* REST API integration
* Database storage for extracted records

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repository and submit a pull request.


## 👨‍💻 Author

**Prem Ramdas Chavan**

If you found this project useful, consider giving it a ⭐ on GitHub.
