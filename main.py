from sport.api import BasketballSport
from pprint import pprint as pp

token = "1000001077:26f482b511af40a591eb5372924d3dd9"
basketball = BasketballSport(token, debug=True)
pp(basketball.live())
# print(len(basketball.live()))