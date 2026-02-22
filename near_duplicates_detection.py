import sys #sys is a built-in Python module that lets you: Access command line arguments , Exit the program
import requests 
from bs4 import BeautifulSoup
from collections import Counter
import re

print("Length:", len(sys.argv))
# argv  is Argument vector stores command line arguments 
# python scraper.py https://www.sitare.org -> argv = ["scraper.py", "https://www.sitare.org "]
if len(sys.argv)!=3: # wrong input or didn't give url
    print("Usage: python scraper.py <URL>")
    sys.exit(1) #stop programm, 1 means -> exit with error , 0-> success
url1 = sys.argv[1]
url2= sys.argv[2]



def compute_simhash_from_url(url):

    
    response = requests.get(url)  #Sends an HTTP GET request to the server, Gets HTML content , Wraps everything inside a response object
    if response.status_code !=200:
        print("failed to fetch the page")
        sys.exit(1)
    html_content = response.text
    soup = BeautifulSoup(html_content,"html.parser")
    #extract page body text
    body = body = soup.body.get_text() if soup.body else "No body found"
    text = body.lower()
    # extract only alphanumeric words
    wordList = re.findall(r'\b[a-z0-9]+\b', text)
    frequency = Counter(wordList)
    return compute_simhash(frequency)




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
    lst = [0]*64

    for word, count in frequency.items():
        h = polynomial_hash(word)

        for i in range(64):
            if h & (1<<i):
                lst[i]+=count
            else :
                lst[i]-=count

    #build final hash
    simhash =0
    for i in range(64):
        if lst[i]>0:
            simhash = simhash | (1<<i)
    return simhash
    

simhash_value_url1 = compute_simhash_from_url(url1)
simhash_value_url2 = compute_simhash_from_url(url2)

def count_common_bits(hash1, hash2):
    xor = hash1 ^ hash2   # XOR gives 1 where bits differ
    diff_bits = bin(xor).count("1")
    return 64 - diff_bits

common_bits = count_common_bits(simhash_value_url1, simhash_value_url2)

print("\nCommon bits between URLs:", common_bits)

