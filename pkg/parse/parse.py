import json

from pkg.parse.portfolio_option import PortfolioOption


def parse_from_importer():
    with open('data.json') as json_file:
        data = json.load(json_file)
        pos = {}
        for d in data:
            pos[d['ticker']] = PortfolioOption(d)
        return pos
