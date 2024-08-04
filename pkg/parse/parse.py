import json

from pkg.parse.portfolio_option import PortfolioOption


def parse_from_importer(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        return get_portfolio_option_from_data(data)


def get_portfolio_option_from_data(data):
    pos = {}
    for key in data:
        pos[key] = PortfolioOption(data[key])
    return pos
