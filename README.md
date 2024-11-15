# Article Generator

A simple Python application that converts text articles into HTML format using OpenAI GPT-4.

## Quick Start

1. Clone the repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

4. Prepare your article in `article.txt` file

5. Run the application:
```bash
python main.py
```

The processed article will be saved as `artykul.html`

## Viewing the Result
The repository has also two files:

`artykul.html` - contains just the article content

`szablon.html` - sheet for article styling

### To view your styled article:

1. Open `artykul.html`
2. Copy everything between <!-- Tutaj zostanie wklejona treść wygenerowanego artykułu --> comments
3. Paste it into `szablon.html` between body html tags
4. Save as `podglad.html`
5. Open `podglad.html` in your browser to see the styled version


*Generating article can take some time, so please be patient. :)*
