from bs4 import BeautifulSoup
import requests
import threading
import time
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

############################################################################# print 

def get_titles_numbered():
  time.sleep(0.3)
  post_titles = soup.find_all(name="td", class_="title")
  counter = 0
  for i in post_titles:
    if counter < 1 :
      counter += 1
      print(i.getText(), end="")
    else:
      counter = 0
      print(i.getText())
    

def get_titles():
  time.sleep(0.3)
  post_titles = soup.find_all(class_="titleline")
  for i in post_titles:
    print(i.getText())
  

def get_article_upvote():
  time.sleep(0.3)
  post_titles = soup.find_all(name="span", class_="score")
  for i in post_titles:
    print(i.getText())
  

def get_href():
  post_titles = soup.find_all(class_="titleline")
  for i in post_titles:
    print(i.find('a').get('href'))
  
  
get_titles_numbered()
get_article_upvote()
get_href()

# thread1 = threading.Thread(target=get_titles_numbered)
# thread2 = threading.Thread(target=get_article_upvote)


# thread1.start()
# thread2.start()


# thread1.join()
# thread2.join()



############################################################################# concatenated 
# link = soup.select('span').find('a')
# print(link)
# for i in post_titles:
#   print(f' record {i}')


# import lxml
# with open("./bs4-start/website.html", mode="r") as website:
#   contents = website.read()
 

#   soup = BeautifulSoup(contents, "html.parser")
#   # print(soup.li)
#   all_anchor_tags = soup.find_all(name="a")

#   for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
  
# heading = soup.find(name="h1", id="name")
# print(heading)
# print(all_anchor_tags)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get_text)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# company_url = soup.select_one(selector="#name")
# print(company_url)

# headings = soup.select(".heading")
# print(heading)