from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

def main():
    currency_type = str(sys.argv[1])

    url = 'http://www.boc.cn/sourcedb/whpj/enindex.html'
    html = urlopen(url).read().decode('utf8')

    soup = BeautifulSoup(html, features='lxml')
    all_tables = soup.find('table', width='600')
    all_rows = all_tables.findChildren('tr')

    currency_dict = {row.findChildren('td')[0].string : list_to_dict(row.findChildren('td')) for row in all_rows[2:]}

    print(currency_dict.get(currency_type))

def list_to_dict(row):
    return {'Buying Rate': row[1].string, 'Cash Buying Rate': row[2].string,
            'Selling Rate': row[3].string, 'Cash Selling Rate': row[4].string,
            'Middle Rate': row[5].string}

if __name__ == '__main__':
    main()










