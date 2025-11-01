import requests
from .models import GoogleBook
from django.conf import settings

GOOGLE_BOOKS_API_KEY = getattr(settings, "GOOGLE_BOOKS_API_KEY", "")

def fetch_books(query="JavaScript", max_results=12):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "maxResults": max_results,
        "key": GOOGLE_BOOKS_API_KEY,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        items = data.get("items", [])
        if not items:
            print("No books found from Google API.")
            return

    except requests.RequestException as e:
        print(f"Error fetching books from Google API: {e}")
        return

    count = 0
    for item in items:
        info = item.get("volumeInfo", {})
        authors = ", ".join(info.get("authors", [])) if info.get("authors") else ""
        categories = ", ".join(info.get("categories", [])) if info.get("categories") else ""

        GoogleBook.objects.update_or_create(
            title=info.get("title", "Unknown Title"),
            defaults={
                "authors": authors,
                "publisher": info.get("publisher", ""),
                "published_date": info.get("publishedDate", ""),
                "description": info.get("description", ""),
                "page_count": info.get("pageCount") or 0,
                "categories": categories,
                "thumbnail": info.get("imageLinks", {}).get("thumbnail", ""),
                "preview_link": info.get("previewLink", "")
            }
        )
        count += 1

    print(f"{count} books fetched and updated successfully from query '{query}'.")
