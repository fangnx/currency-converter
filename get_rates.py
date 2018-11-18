from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

RATE_TYPES = ["Buying Rate", "Cash Buying Rate", "Selling Rate", "Cash Selling Rate", "Middle Rate"]


def main():

    # currency_type = input("Enter the currency type: ")
    currency_type = "CAD"

    currency_dict = get_all_rates()

    print_all_rates(currency_dict, currency_type)


def get_all_rates():

    url = "http://www.boc.cn/sourcedb/whpj/enindex.html"
    html = urlopen(url).read().decode('utf8')

    soup = BeautifulSoup(html, features="lxml")
    all_tables = soup.find("table", width="600")
    all_rows = all_tables.findChildren("tr")

    # Store the currency rates in a dictionary
    currency_dict = {row.findChildren("td")[0].string: row.findChildren("td") for row in all_rows[2:]}

    return currency_dict


def to_string(currency_dict, currency_type):

    output = ""

    currency_row = currency_dict.get(currency_type)
    for i, type_name in enumerate(RATE_TYPES):
        output += (type_name + ": " + currency_row[i + 1].string)

    return output





def print_all_rates(dict, type):

    currency_row = dict.get(type)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The exchange rate from " + type + " to RMB:\n")

    for i, type_name in enumerate(RATE_TYPES):
        print(type_name + ": " + currency_row[i+1].string)
    print("\nPublish Time: " + currency_row[6].string)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == '__main__':
    main()










