import requests


def check_book(query):
    url = f"https://openlibrary.org/search.json?q={query}"
    response = requests.get(url)
    data = response.json()
    
    book = data["docs"][0]
    return f"{book['title']} by {book['author_name'][0]}"

print(check_book("harry potter"))
