import requests
from bs4 import BeautifulSoup as bs

from tqdm import tqdm


def innerpage_links(tag, cls, i_tag, i_cls):
    links_list = []

    for i in tqdm(range(1, 10)):
        url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=b83d8fba-7863-4d7b-8b1c-87a582b667dd&page={0}".format(
            i)
        response = requests.get(url)
        soup = bs(response.text)

        for i in soup.find_all(tag, class_=cls):
            c = i.find(i_tag, class_=i_cls)["href"]
            flip = "https://www.flipkart.com" + c
            links_list.append(flip)
    return links_list


def details(links):
    flip_list = []
    for x in tqdm(links):
        response = requests.get(x)
        soup = bs(response.text)

        for i in soup.find_all("div", class_="aMaAEs"):

            name = i.find("span", class_="B_NuCI")
            if name is None:
                name = "no value"
            else:
                name = name.text

            r = i.find("div", class_="_3LWZlK")
            if r is None:
                r = "no value"
            else:
                r = r.text

            re = i.find("span", class_="_2_R_DZ")
            if re is None:
                re = "no value"
            else:
                re = re.text

            e = i.find("div", class_="_1V_ZGU")
            if e is None:
                e = "no value"
            else:
                e = e.text

            p = i.find("div", class_="_30jeq3 _16Jk6d")
            if p is None:
                p = "no value"
            else:
                p = p.text

            data = (name, r, re, e, p, x)
            flip_list.append(data)
    return flip_list