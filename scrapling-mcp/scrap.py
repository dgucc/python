from scrapling.fetchers import Fetcher
import ollama

# Fetch webpage
page = Fetcher.get('https://www.rtbf.be/la-une')

# Extract text from paragraph tags and limit to 4000 chars
page_text = ' '.join(page.css('p::text').getall())[:4000]

# Send content to Ollama for summarization
response = ollama.chat(
    model="gemma3",
    messages=[
        {
            'role': 'user',
            'content': f"Résume le sujet de ce site web et énumère les principaux thèmes qui y sont abordés.\n\n:{page_text}"           
        }
    ]
)

# Print the response
print(response['message']['content'])
