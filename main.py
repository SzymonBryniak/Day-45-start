from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup)

def get_titles1():
  post_titles = soup.find_all("td")
  print(len(post_titles))
  for i in range(len(post_titles)):
    print(post_titles[i].find_all("a"))


def get_titles2():
  post_titles = soup.soup.find_all(name="td", class_="headtitle")
  print(post_titles)

def get_titles3():
  
  post_titles = soup.find_all("a")
  for i in post_titles:
    print(i.get("href"))
  # print(soup.select_one(selector="span a"))

get_titles3()
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