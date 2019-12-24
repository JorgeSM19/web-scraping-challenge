#Import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
from urllib.parse import urljoin


#NASA Mars News
#!which chromedriver
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

my_dict = {}

def scrape():
    def scrp0():
        url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        news = soup.find_all('ul', class_='item_list')
        for new in news:
            news_title = new.find('div', class_='content_title').text
            news_p = new.find('a').text
            #print('---'*3)
            #print(news_title)
            #print(news_p)
            my_dict["title"] = {}
            my_dict["title"] = news_title
            my_dict["Paragraph"] = {}
            my_dict["Paragraph"] = news_p
    scrp0()

    # JPL Mars Space Images - Featured Image
    def scrp1():
        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        featured_mars_image = soup.find_all('div', class_='img')
        #print('---'*3)
        #print("featured_mars_image: " + featured_mars_image[0].img["src"])
        my_dict["Image"] = {}
        my_dict["Image"] = featured_mars_image[0].img["src"]
    scrp1()

    # Mars Weather
    def scrp2():
        url = "https://twitter.com/marswxreport?lang=en"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()
        #print('---'*3)
        #print(mars_weather)
        my_dict["Weather"] = {}
        my_dict["Weather"] = mars_weather
        
    scrp2()

    #Mars Facts
    def scrp3():
        url = "https://space-facts.com/mars/"
        mars_tables = pd.read_html(url)
        mars_tables
        type(mars_tables)
        mars_facts_df = mars_tables[0]
        mars_facts_df.columns = ['Description', 'Value']
        mars_facts_df.head()
        mars_facts_df.set_index('Description', inplace=True)
        mars_facts_df.head()
        html_mars = mars_facts_df.to_html('mars_table.html')
        html_mars
        #print('---'*3)
        #print(html_mars)
        my_dict["facts"] = {}
        my_dict["facts"] = html_mars

    scrp3()

    def scrp4():
        hemisphere =[]
        hemisphere_list=['Cerberus','Schiaparelli','Syrtis','Valles']
        for hemi in hemisphere_list:
            hemispheres={}
            url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
            browser.visit(url)
            html = browser.html
            soup = BeautifulSoup(html,'html.parser')
            browser.click_link_by_partial_text(hemi)
            html = browser.html
            soup = BeautifulSoup(html,'html.parser')
            hemispheres['image']=soup.find('a',target="_blank")['href']
            hemispheres['title']=soup.find('h2',class_="title").text
            hemisphere.append(hemispheres)
            #print('---'*3)
            #print(hemisphere)
            my_dict["Hemi"] = {}
            my_dict["Hemi"] = hemisphere
    scrp4()
    browser.quit()
    return my_dict
#scrape()

#print(my_dict)