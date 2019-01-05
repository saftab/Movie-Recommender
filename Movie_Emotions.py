from bs4 import BeautifulSoup as SOUP
import re
import lxml
import requests as HTTP

def main(emotions):
    if emotions == "Sad":
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

    elif emotions == "Disgust":
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

    elif emotions == "Anger":
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

    elif emotions == "Anticipation":
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    response = HTTP.get(urlhere)
    data = response.text

    soup = SOUP(data, "lxml")


    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    return title

if __name__ == '__main__':
        emotions = input("Enter the emotion: ")
        a = main(emotions)
        count = 0

        if(emotions == "Anger" or emotions == "Anticipation"):
            for i in a:
                tmp = str(i).split('>')

                if len(tmp) == 3:
                    print(tmp[1][:-3])

                if count > 13:
                    break
                count += 1

        else:
            for i in a:
                tmp = str(i).split('>')

                if len(tmp) == 3:
                    print(tmp[1][:-3])

                if count > 19:
                    break
                count += 1






