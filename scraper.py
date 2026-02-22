import sys #sys is a built-in Python module that lets you: Access command line arguments , Exit the program
import requests 
from bs4 import BeautifulSoup
from collections import Counter
import re


# argv  is Argument vector stores command line arguments 
# python scraper.py https://www.sitare.org -> argv = ["scraper.py", "https://www.sitare.org "]
if len(sys.argv)!=2: # wrong input or didn't give url
    print("Usage: python scraper.py <URL>")
    sys.exit(1) #stop programm, 1 means -> exit with error , 0-> success
url = sys.argv[1]
print("url entered", url)



# fetch the page
response = requests.get(url)  #Sends an HTTP GET request to the server, Gets HTML content , Wraps everything inside a response object


if response.status_code !=200:
    print("failed to fetch the page")
    sys.exit(1)
html_content = response.text



#Parse HTML Using BeautifulSoup
soup = BeautifulSoup(html_content,"html.parser")


# extract page title
title = soup.title.string if soup.title else "No title"
print("Page Title:")
# print(title)
print()



#extract page body text
print("Page body:")
body = soup.body.get_text() if soup.body else "No body found"
# print(body)
print()



#extract all urls
print("All urls:")
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        print(href)



#count frequency of words 
text = body.lower()

# extract only alphanumeric words
wordList = re.findall(r'\b[a-z0-9]+\b', text)

frequency = Counter(wordList)

# print(frequency)



# compute hash for each words
def polynomial_hash(word):
    p=53
    m=1<<64
    hash_value =0
    power=1

    for char  in word:
        hash_value = (hash_value+ord(char)*power) &(m-1)
        power = (power*p)&(m-1)
    return hash_value


#compute simHash 

def compute_simhash(frequency):
    list = [0]*64

    for word, count in frequency.items():
        hash = polynomial_hash(word)

        for i in range(64):
            if hash & (1<<i):
                list[i]+=count
            else :
                list[i]-=count

    #build final hash
    simhash =0
    for i in range(64):
        if list[i]>0:
            simhash = simhash | (1<<i)
    return simhash
    

simhash_value = compute_simhash(frequency)

print("\nSimHash (64-bit):")
print(simhash_value)
print("Binary:")
print(bin(simhash_value))

