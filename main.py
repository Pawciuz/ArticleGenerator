import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ArticleProcessor:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def read_article(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise Exception(f"Nie znaleziono pliku: {file_path}")
        except Exception as e:
            raise Exception(f"Błąd podczas odczytu pliku: {str(e)}")

    def process_article(self, content):
        prompt = """
        Przekształć poniższy artykuł w kod HTML spełniający następujące wymagania:
        1. Użyj odpowiednich tagów HTML do strukturyzacji treści
        2. Zidentyfikuj miejsca na grafiki i wstaw placeholdery z następującym formatem:
           <img src="image_placeholder.jpg" alt="[DOKŁADNY PROMPT DO WYGENEROWANIA GRAFIKI]">
           Pod każdą grafiką dodaj odpowiedni podpis używając tagu <figcaption>
        3. Nie dodawaj CSS ani JavaScript
        4. Nie dodawaj tagów html, head, body - zwróć tylko zawartość sekcji body

        Oto artykuł do przetworzenia:

        {content}
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Jesteś ekspertem od strukturyzacji treści w HTML."},
                    {"role": "user", "content": prompt.format(content=content)}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Błąd podczas przetwarzania przez OpenAI: {str(e)}")

    def save_html(self, html_content, output_path):
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(html_content)
        except Exception as e:
            raise Exception(f"Błąd podczas zapisywania pliku HTML: {str(e)}")


def main():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise Exception("Nie znaleziono klucza API OpenAI w zmiennych środowiskowych")

    processor = ArticleProcessor(api_key)

    input_file = "article.txt"  # Zmień na właściwą ścieżkę
    output_file = "artykul.html"

    try:
        content = processor.read_article(input_file)

        html_content = processor.process_article(content)

        processor.save_html(html_content, output_file)

        print(f"Artykuł został pomyślnie przetworzony i zapisany w {output_file}")

    except Exception as e:
        print(f"Wystąpił błąd: {str(e)}")


if __name__ == "__main__":
    main()