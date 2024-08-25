import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# List of URLs to scrape
url_list = ['https://phys.org/technology-news/quantum-computing/',
            'https://quantumcomputingreport.com/',
            'https://thequantumdaily.com/',
            'https://thequantumdaily.com/',
            'https://www.sciencedaily.com/news/computers_math/quantum_computers/',
            'https://thequantuminsider.com/'
]

def fetch_articles(urls):
    extracted_data = []

    for i in urls:
        response = requests.get(i)

        try:
            print(f"Fetching {i}")

            if response.status_code == 200:
                print("Successfully fetched the webpage!")
                soup = BeautifulSoup(response.content, 'html.parser')
                articles = soup.find_all('article')

                for article in articles:
                    title = article.find('h2').text.strip() if article.find('h2') else 'No title found'
                    link = article.find('a')['href'] if article.find('a') else 'No link found'

                    # Find the publication date
                    date_str = article.find('time').text.strip() if article.find('time') else 'No date found'

                    # Convert the date string to a datetime object
                    pub_date = None
                    try:
                        pub_date = datetime.strptime(date_str, '%d %b %Y') if date_str != 'No date found' else None
                    except ValueError:
                        print(f"Date parsing failed for article: {title}")
                        continue

                    # Check if the article was published in the last two weeks
                    if pub_date and datetime.now() - pub_date <= timedelta(weeks=5):
                        extracted_data.append({
                            'title': title,
                            'link': link,
                            'date': pub_date.strftime('%Y-%m-%d')
                        })

            else:
                print(f"Failed to fetch the webpage. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred: {e}")

    return extracted_data

def save_to_csv(data, filename='quantum_news.csv'):
    with open(filename, 'w') as file:
        file.write("Title,Link,Date\n")
        for item in data:
            file.write(f"{item['title']},{item['link']},{item['date']}\n")

# Example usage
articles_data = fetch_articles(url_list)
if articles_data:
    save_to_csv(articles_data)
    print(f"Saved {len(articles_data)} articles to CSV.")
else:
    print("No articles found in the last week.")
