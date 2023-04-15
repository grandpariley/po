import json

from pkg.parse.portfolio_option import PortfolioOption


def parse_from_importer():
    with open('data.json') as json_file:
        data = json.load(json_file)
        pos = {}
        for key in data:
            pos[key] = PortfolioOption(data[key])
        return pos
