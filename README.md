
# Auto News Generator

`auto_newsgenerator` is a Python script that fetches news articles using the News API, focused on specific keywords. The script outputs news in a WhatsApp-friendly format, making it ideal for sharing industry updates in messaging platforms.

## Features

- Fetches the latest news based on user-defined topics.
- Outputs news in a format suitable for WhatsApp or similar platforms.
- Supports customization of search queries, number of articles, language, and sorting.

## Requirements

- Python 3.8+
- News API key (available from [News API](https://newsapi.org/))

### Dependencies

Install the required dependencies:

```bash
pip install requests
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/auto_newsgenerator.git
   cd auto_newsgenerator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your News API key:
   Replace `"YOUR_API_KEY"` in the script with your actual API key from [News API](https://newsapi.org/).

## Customizing the Script

You can customize the following settings directly in the script:

### 1. **Keywords (Topics)**

Modify the `q` parameter to change the topics being searched for:

```python
'q': 'quantum computing OR quantum technology OR quantum cryptography'
```

For example, to search for climate change news:

```python
'q': 'climate change OR global warming'
```

### 2. **Number of Articles**

Adjust the number of articles fetched per request using the `pageSize` parameter:

```python
'pageSize': 50  # Fetch up to 50 articles
```

Change it to any number within News API's limits (1-100):

```python
'pageSize': 20  # Fetch 20 articles
```

### 3. **Language**

Change the language of the articles by modifying the `language` parameter:

```python
'language': 'en'  # Fetch only English articles
```

Other options include `es` (Spanish), `fr` (French), etc.

### 4. **Sort By**

Customize how articles are sorted with the `sortBy` parameter:

```python
'sortBy': 'publishedAt'  # Sort by the latest articles
```

Other options include:
- `relevancy` – articles more closely related to the query.
- `popularity` – articles from popular sources.

### Example Custom Parameters

```python
params = {
    'q': 'artificial intelligence OR AI OR machine learning',
    'sortBy': 'relevancy',
    'language': 'es',
    'pageSize': 30,
    'apiKey': api_key
}
```

## Usage

To generate news on a specific topic, run the script:

```bash
python auto_newsgenerator.py
```

### Sample  Output

```
📰 *Quantum Industry News Update*

1. *New Breakthrough in Quantum Computing* - [Read more](https://example.com/quantum-breakthrough)
   *Source*: BBC News

2. *Quantum Cryptography's Role in Cybersecurity* - [Read more](https://example.com/quantum-cryptography)
   *Source*: TechCrunch

📅 Stay updated every Monday with One Quantum!
```

## Error Handling

If the script encounters issues while fetching articles, it will return an error message with the status code:

```bash
Failed to fetch news articles. Status Code: 403
```

## Contributing

Feel free to submit issues or pull requests for improvements, new features, or bug fixes. Contributions are always welcome!
