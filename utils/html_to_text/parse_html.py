from bs4 import BeautifulSoup


def parse_html(html):
    elem = BeautifulSoup(html, features="html.parser")
    text = ''
    for e in elem.descendants:
        if isinstance(e, str):
            text += e.strip()
        elif e.name in ['br',  'p', 'h1', 'h2', 'h3', 'h4', 'tr', 'th']:
            text += '\n'
        elif e.name == 'li':
            text += '\n- '
    return text
