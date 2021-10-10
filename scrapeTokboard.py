from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pprint


def main():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--enable-javascript")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get('https://www.tokboard.com/')

    c = True
    while c:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.find(class_='jsx-2291293095')
        if table.get_text():
            c = False

    pp = pprint.PrettyPrinter(indent=4)

    results_artists = table.find_all(attrs={'class': 'jsx-3696330819 artist'})
    list_artist = []
    for result in results_artists:
        artist = result.get_text()
        list_artist.append(artist)

    list_title = []
    results_titles = table.find_all(attrs={'class': 'jsx-3696330819 title'})
    for result_title in results_titles:
        title = result_title.get_text()
        list_title.append(title)

    final_list = dict(zip(list_artist, list_title))
    pp.pprint(final_list)


def scrapeTokboard():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--enable-javascript")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get('https://www.tokboard.com/')

    c = True
    while c:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.find(class_='jsx-2291293095')
        if table.get_text():
            c = False

    results_artists = table.find_all(attrs={'class': 'jsx-3696330819 artist'})
    list_artist = []
    for result in results_artists:
        artist = result.get_text()
        list_artist.append(artist)

    list_title = []
    results_titles = table.find_all(attrs={'class': 'jsx-3696330819 title'})
    for result_title in results_titles:
        title = result_title.get_text()
        list_title.append(title)

    final_list = dict(zip(list_artist, list_title))
    return final_list

if __name__ == '__main__':
    main()
