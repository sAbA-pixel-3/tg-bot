# prsing for sqlalchemy
# from databases.querysets import *
from bs4 import BeautifulSoup as BS
import requests



# def get_html(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'}
#     r = requests.get(url, headers=headers) 
#     if r.status_code == 200:
#         return r.text
#     else: 
#         return None
    

# def get_movie_data(html):
#     soup = BS(html, 'html.parser')
#     main_data = soup.find_all('div', class_="article-detail__content")
#     movies = [] 
#     for data in main_data:
#         titles = data.find('div',class_ = 'article-detail_tag article-detail_tag_h2')
#         if titles == None:
#             continue
#         else: 
#             titles2 = data.find_all('div',
#             class_ = 'article-detail_tag article-detail_tag_h2')
#             for title2 in titles2:
#                 title = title2.text.strip()
#         country2 = data.find('div', 
#             class_ = 'article-detail_tag article-detail_tag_p')
#         if country2 == None:
#             continue
#         else:
#             country2 = data.find_all('article', 
#             class_ = 'article-detail_tag article-detail_tag_p')
#             for country3 in country2:
#                 if 'Страна' in country3.text.strip():
#                     country = country3.text.strip()
#                 if 'В ролях' in country3.text.strip():
#                     actors = country3.text.strip() 
#         images = data.find_all('div',
#         class_="article-element article-element_images")
#         if images == None:
#             continue
#         else:
#             images2 = data.find_all('div',
#              class_="article-element article-element_images")
#             for image2 in images2:
#                 image = image2.find('img').get('src')


#     movies.append({
#         'title': title,
#         'country': country,
#         'description': actors,
#         'trailer': image,
#         'age_limit': 18,
#         'release_date': '2020-13-23',
#         'image': image,
#         'url': 2})  
#     return movies 



    
def parsing_main():
    url = "https://www.pravilamag.ru/entertainment/672783-100-luchshih-filmov-vseh-vremen-vybor-amerikanskogo-esquire/"
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'}
    r = requests.get(url, headers=headers) 
    get_movie_data(r.text)  

# if __name__ == "__main__":
#     main() 

def get_movie_data(html):
    soup = BS(html, 'html.parser')
    main_data = soup.find_all('div', class_="article-detail__content")
    movies = [] 
    for data in main_data:
        titles = data.find('div',class_ = 'article-detail_tag article-detail_tag_h2')
        if titles == None:
            continue
        else: 
            titles2 = data.find_all('div',
            class_ = 'article-detail_tag article-detail_tag_h2')
            for title2 in titles2:
                title = title2.text.strip()
        country2 = data.find('div', 
            class_ = 'article-detail_tag article-detail_tag_p')
        if country2 == None:
            continue
        else:
            country2 = data.find_all('article', 
            class_ = 'article-detail_tag article-detail_tag_p')
            for country3 in country2:
                if 'Страна' in country3.text.strip():
                    country = country3.text.strip()
                if 'В ролях' in country3.text.strip():
                    actors = country3.text.strip() 
        images = data.find_all('div',
        class_="article-element article-element_images")
        if images == None:
            continue
        else:
            images2 = data.find_all('div',
             class_="article-element article-element_images")
            for image2 in images2:
                image = image2.find('img').get('src')
                trailer = 'https://www.galvanizeaction.org/the-pyschology-of-gifs/'


        movies.append({
        'title': title,
        'country': country,
        'description': actors,
        'trailer': trailer, 
        'age_limit': 18,
        'release_date': '2020-13-23',
        'image': image,
        'url': 2})  
    return movies









