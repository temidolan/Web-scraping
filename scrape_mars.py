



# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape():
    browser = init_browser()
    usgs_dict={}

# Visit Nasa news url through splinter module
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html= browser.html
    soup= bs(html, 'html.parser')

    
    usgs_dict["news_title"] = soup.find("div", class_='content_title').get_text()
    usgs_dict["news_p"]= soup.find('div', class_='article_teaser_body').get_text()



# Visit the url for JPL Featured Space Image
    url_image="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)
    browser.click_link_by_partial_text('FULL IMAGE')
    expand = browser.find_by_css('a.fancybox-expand')



    html_image = browser.html
    soup = bs(html_image, 'html.parser')


    featured_image_url= soup.find("img",{"class":"fancybox-image"})["src"]

    mainurl="https://www.jpl.nasa.gov"

    original_image_url= mainurl + featured_image_url
    usgs_dict["featured_url"] = original_image_url




    web_url= "https://space-facts.com/mars/"
    browser.visit(web_url)
    html_web=browser.html
    soup=bs(html_web, "html.parser")



    tables = pd.read_html(web_url)
    tables




    df1=tables[0]
    df1

    df2=tables[1]
    df2



    df1.columns= ["Elements","Facts/Observations"]
    df1


    df1['Elements'][0]

    df1.set_index("Elements", inplace= True)
    df1.head()


    html_table = df1.to_html()
    html_table
    html_table.replace('\n', '')
    usgs_dict["html_info"]=html_table




    # mars_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # mars_link="/Users/kumba/Desktop/1usgs.html"
    # browser.visit(mars_url)
    # html_mars=browser.html
    # soup=bs(html_mars, "html.parser")

    return usgs_dict