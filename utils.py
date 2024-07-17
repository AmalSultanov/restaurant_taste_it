import requests
from bs4 import BeautifulSoup


def get_referer_title(request):
    referer_url = request.META.get('HTTP_REFERER', '')
    referer_title = ''

    if referer_url:
        try:
            response = requests.get(referer_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                referer_title = soup.title.string if soup.title else 'Title not found'
            else:
                print(
                    f'Failed to retrieve the page: {response.status_code}')
        except Exception as e:
            print(f'An error occurred: {e}')

    return referer_title
