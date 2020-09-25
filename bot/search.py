from googlesearch import search

"""
using search from  google python package, pip install google,
we can user google search console api (legacy) in future 
"""


def search_google(query, **kwargs):
    """
    search function which provide the result to user query, and having config/filter value
    set it up
    :param query: user search query ie !google <search query>
    :param kwargs: config/filter to provide result from google
    :return: generator object of found search link
    """
    if not query:
        return "No search query found"
    for obj in search(query, **kwargs):
        yield obj
