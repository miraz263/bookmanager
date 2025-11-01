from django.http import JsonResponse
from .models import GoogleBook
from .utils import fetch_books

def import_books_view(request):
    query = request.GET.get("q", "Python Programming")
    fetch_flag = request.GET.get("fetch", "true").lower() == "true"

    try:
        max_results = int(request.GET.get("max_results", 5))
        if max_results < 1:
            max_results = 5
    except ValueError:
        max_results = 5

    try:
        if fetch_flag:
            fetch_books(query=query, max_results=max_results)

        books = list(
            GoogleBook.objects.all().values(
                "title", "authors", "publisher", "published_date",
                "description", "page_count", "categories",
                "thumbnail", "preview_link"
            )
        )

        return JsonResponse({"status": "success", "books": books})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


def books_json(request):
    books = list(
        GoogleBook.objects.all().values(
            "title", "authors", "publisher", "published_date",
            "description", "page_count", "categories",
            "thumbnail", "preview_link"
        )
    )
    return JsonResponse({"status": "success", "books": books})
