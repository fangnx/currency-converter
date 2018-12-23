import requests
from bs4 import BeautifulSoup
from ast import literal_eval


def get_all_curr_types():

    url = "https://www.x-rates.com/table/?from=USD&amount=1"
    raw_content = requests.get(url).text
    soup = BeautifulSoup(raw_content, "lxml")
    chart = soup.find("select", class_="ccDbx").find_all("option")
    curr_type_list = [c.string.split(" - ") for c in chart]

    return curr_type_list


def get_rates(base_curr):

    url = "https://www.x-rates.com/table/?from=" + base_curr + "&amount=1"
    get = requests.get(url)
    if get.status_code != requests.codes.ok:
        return -1

    raw_content = get.text
    soup = BeautifulSoup(raw_content, "lxml")
    table = soup.find("table", class_="tablesorter ratesTable").find_all("tr")

    curr_rates = {}
    for t in table[1::]:
        cells = t.find_all("td")
        type = cells[0].get_text()
        rate = cells[1].a.get_text()
        curr_rates[type] = rate

    return curr_rates


def get_montly_avg(base_curr, target_curr, year):

    url = "https://www.x-rates.com/average/?from=" + base_curr \
          + "&to=" + target_curr + "&amount=1&year=" + str(year)

    raw_content = requests.get(url).text
    soup = BeautifulSoup(raw_content, "lxml")
    avg_list = soup.find_all("ul", class_="OutputLinksAvg")

    avg_rates = {line.find("span", class_="avgMonth").get_text():
                     line.find("span", class_="avgRate").get_text()
                 for line in avg_list[0].find_all("li")}

    return avg_rates


def calculate_float(rate, amt):
    return literal_eval(rate) * amt




