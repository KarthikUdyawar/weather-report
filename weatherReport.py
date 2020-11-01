# import
import requests
from bs4 import BeautifulSoup

# fecting function
def weather(location):
    url = f"https://www.google.com/search?&q=weather in {location}"
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    temp = s.find("div",class_="BNeawe").text
    return temp

# main function
if __name__ =="__main__":
    location = input("Enter location : ")
    if location == "":
        location = "your location"
    print(f"Current temperature in {location}: {weather(location)}")
