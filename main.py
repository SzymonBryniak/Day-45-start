from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")


def get_titles():
  
  post_titles = soup.find_all(name="td", class_="title")
  counter = 0
  for i in post_titles:
    if counter < 1 :
      counter += 1
      print(i.getText(), end="")
      print(i)
    else:
      counter = 0
      print(i.getText())
  # print(soup.select_one(selector="span a"))

def get_article_upvote():
  
  post_titles = soup.find_all(name="span", class_="score")
  counter = 0
  for i in post_titles:
    print(i.getText())
    
  # print(soup.select_one(selector="span"))

def get_href():
  
  # post_titles = soup.find_all(name="a")
  # counter = 0
  # for i in post_titles:  
  #   print(i)
  span = soup.select('span', class_="titleline")
  children = soup.find_all(True)
  print(children)


def get_titles_href():
  
  post_titles = soup.find_all(name="span", class_="titleline")
  counter = 0
  for i in post_titles:
    if counter < 1 :
      counter += 1
      print(i, end="")
  
    else:
      counter = 0
      print(i.getText())

get_titles_href()

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