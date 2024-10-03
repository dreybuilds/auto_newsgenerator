import requests

# Your NewsAPI key
api_key = '36bee74a3fce488daac72f84201183cb'  # Replace with your actual API key

# Base URL for the API
url = 'https://newsapi.org/v2/everything'

# Define the parameters for the API request
params = {
    'q': 'quantum computing OR quantum technology OR quantum cryptography',  # Keywords
    'sortBy': 'publishedAt',  # Sort by latest news
    'language': 'en',  # Language of the articles
    'pageSize': 50,  # Number of articles per request
    'apiKey': api_key
}

# Make the request
response = requests.get(url, params=params)

# Check for a successful request
if response.status_code == 200:
    articles = response.json().get('articles')
    if articles:
        # Generate WhatsApp-friendly text
        whatsapp_text = "📰 *Quantum Industry News Update*\n\n"
        
        for i, article in enumerate(articles, 1):
            title = article['title']
            source = article['source']['name']
            url = article['url']
            # Combine title and link for WhatsApp
            whatsapp_text += f"{i}. *{title}* - [Read more]({url})\n   *Source*: {source}\n\n"
        
        whatsapp_text += "📅 Stay updated every Monday with One Quantum!"
        print(whatsapp_text)
    else:
        print("No articles found for the given query.")
else:
    print(f"Failed to fetch news articles. Status Code: {response.status_code}")
