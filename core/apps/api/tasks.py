import os
import uuid
import shutil
import requests
from bs4 import BeautifulSoup
from django.utils.text import slugify
from celery import shared_task

from core.apps.api.models import CategoryModel, ProductModel

from celery import shared_task
from bs4 import BeautifulSoup
from django.utils.text import slugify
from core.apps.api.models import CategoryModel, ProductModel

import os
import uuid
import shutil
import requests




def download_image(url, folder="media/product/"):
    if not url:
        print("❌ URL yo‘q, rasm yuklanmadi.")
        return None

    os.makedirs(folder, exist_ok=True)
    filename = f"{uuid.uuid4().hex}{os.path.splitext(url)[-1]}"
    filepath = os.path.join(folder, filename)

    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
            return f"product/{filename}"
    except Exception as e:
        print(f"❌ Rasm yuklashda xatolik: {url} -> {e}")
    return None

def limit_words(text, max_words=100):
    words = text.strip().split()
    return ' '.join(words[:max_words]) + ("..." if len(words) > max_words else "")

@shared_task
def scrape_and_save_products():
    categories = CategoryModel.objects.exclude(url=None)
    all_saved = 0

    headers = {'User-Agent': 'Mozilla/5.0'}

    for category in categories:
        print(f"📂 {category.title} → {category.url}")
        try:
            response = requests.get(category.url, headers=headers)
        except Exception as e:
            print(f"❌ {category.url} ochilmadi: {e}")
            continue

        if response.status_code != 200:
            print(f"❌ {category.url} holat kodi: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        product_links = soup.select(".products-list-tit a")

        print(f"🔗 Topilgan mahsulotlar soni: {len(product_links)}")

        for i, link_tag in enumerate(product_links):
            title = link_tag.get("title", "").strip()
            url = link_tag.get("href", "").strip()

            if not title or not url:
                continue

            try:
                detail = requests.get(url, headers=headers)
            except Exception as e:
                print(f"❌ Mahsulot sahifasi ochilmadi: {url} → {e}")
                continue

            detail_soup = BeautifulSoup(detail.text, "html.parser")

            desc_el = detail_soup.select_one(".pdshow-r-text")
            description = desc_el.get_text(strip=True) if desc_el else ""

            content_el = detail_soup.select_one(".prodetails-bref")
            content = content_el.get_text(separator="\n", strip=True) if content_el else ""

            video_iframe = detail_soup.select_one("iframe")
            video_url = video_iframe["src"] if video_iframe else ""

            subtitle = description.split(".")[0][:200] if description else ""

            images = detail_soup.select(".preview-container img")
            image_url = ""
            for img in images:
                src = img.get("src")
                if src and not 'mediaplay' in img.get("class", []):
                    image_url = src
                    break

            saved_image = download_image(image_url) if image_url else None

            ProductModel.objects.update_or_create(
                title=title,
                category=category,
                defaults={
                    "slug": slugify(title),
                    "subtitle": subtitle,
                    "description": description,
                    "content": limit_words(content),
                    "video_url": video_url,
                    "link": url,
                    "image": saved_image,
                    "rate": 4.5,
                    "is_new": False,
                    "popular": False
                }
            )

            print(f"✅ {i + 1}) {title} saqlandi")
            all_saved += 1

    return f"Jami {all_saved} ta product saqlandi"




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