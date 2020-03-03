from parsel import Selector
from typing import NoReturn
from cliparse.html import text


def execute(xpath: str) -> NoReturn:
    """Prints elements of html file matched by xpath"""
    print(str(xpath))
    print(f'There are the elements of html that match xpath "{str(xpath)}":')
    html_elements = Selector(text).xpath(xpath).get()
    print(html_elements)
