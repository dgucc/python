import ollama
from ddgs import DDGS # DuckDuckGo_Search

ddgs = DDGS()

def search_internet(query):
    try:
        results = ddgs.text(query, max_results=5)
        # Filter out irrelevant results
        filtered_results = [result for result in results if 'body' in result]
        return filtered_results
    except Exception as e:
        print(f"Error searching internet: {e}")
        return []

def get_combined_response(query):
    # Preprocess user input
    query = query.strip().lower()

    # Perform internet search
    search_results = search_internet(query)
    search_content = "\n".join([result['body'] for result in search_results])

    # Integrate search results into the AI response
    try:
        response = ollama.chat(
            model='gemma3',
            messages=[
                {'role': 'user', 'content': query},
                {'role': 'system', 'content': search_content}
            ]
        )
        return response['message']['content']
    except Exception as e:
        print(f"Error generating AI response: {e}")
        return "Sorry, there was an error generating a response for the internet search."


def main():
    query = "Qui est le vainqueur de Formule 1 en 2026?"
    response = get_combined_response(query)

    # Print the search results and the AI response
    search_results = search_internet(query)
    print("Search Results:")
    for result in search_results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['href']}")
        print(f"Snippet: {result['body']}\n")

    print("--------------------------------------------------------")
    print("AI Response:")
    print(response)


if __name__ == '__main__':
    main()