from googlesearch import search


def search_google(query, **kwargs):
    if not query:
        return "No search query found"
    for obj in search(query, **kwargs):
        yield  obj
