# random text generator based on "Яндекс.Рефераты" service
import requests
from random import randint
from bs4 import BeautifulSoup


class Essay(object):
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body

    def __repr__(self):
        return f"{self.subject}\n{self.body}"


def parse_essay(html):
    soup = BeautifulSoup(html, "lxml")
    text = soup.find('div', {"class": "referats__text"})

    # find subject
    subject = text.strong.string[7:-1]

    # remove subject and text description
    text.div.decompose()
    text.strong.decompose()

    # add signature
    greeting = soup.new_tag('h3')
    greeting.string = "Добрый день."
    text.contents.insert(0, greeting)

    stamp = get_stamp(soup)
    text.contents.append(stamp)

    return Essay(subject, text.__str__())


def get_stamp(soup):
    stamp = soup.new_tag('h5')

    respect = soup.new_tag('span')
    respect.string = "С уважением,"
    stamp.append(respect)
    stamp.append(soup.new_tag('br'))

    name = soup.new_tag('span')
    name.string = 'Владимир Владимирович Штец.'
    stamp.append(name)
    stamp.append(soup.new_tag('br'))

    phone = soup.new_tag('span')
    phone.string = 'Телефон: +7 987 654-32-10'
    stamp.append(phone)
    stamp.append(soup.new_tag('br'))

    requisites = soup.new_tag('span')
    requisites.string = 'ИНН-КПП: 6663003127-668601001'
    stamp.append(requisites)

    return stamp


def _get_html(url):
    response = requests.get(url)
    return response.content


def random():
    seed = randint(1000, 99999)
    url = f"https://yandex.ru/referats/?t=psychology+philosophy&s={seed}"
    html = _get_html(url)
    return parse_essay(html)


if __name__ == '__main__':
    essay = random()
    print(essay)
