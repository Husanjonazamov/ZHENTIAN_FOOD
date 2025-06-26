from celery import shared_task
import requests
from bs4 import BeautifulSoup
from core.apps.api.models import CategoryModel


@shared_task
def scrape_example():
    url = "https://www.zt-food.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url=url, headers=headers)
    print("Holat kodi:", response.status_code)
    print("URL:", response.url)

    soup = BeautifulSoup(response.text, "html.parser")

    category_list = soup.select('ul.submenu.nav0 > li.side_nav1 > a')

    print("Topilgan categorylar soni:", len(category_list))

    count = 0
    for a in category_list:
        title = a.get_text(strip=True)
        link = a['href']
        print(f"Kategoriya: {title} -> {link}")

        CategoryModel.objects.update_or_create(
            title=title,
            defaults={'url': link}
        )
        count += 1

    return f"{count} ta kategoriya saqlandi."
