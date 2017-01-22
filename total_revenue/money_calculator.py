# LET'S GO SHOPIFY!!
# This code finds the total revenue I have made as a successful merchant on shopify.
# Looks like my designer shoelaces business has finally taken off!
# It shows the total money made in CAD and USD

import re
import urllib2
from urllib2 import *


def total_in_usd(orders):
    """This function calculates the total in US dollars"""

    # find all the total_price_usd using regex
    # *? non greedy match
    prices = re.findall('total_price_usd":"(.*?)"', orders, flags=0)
    usd_total = get_total(prices)
    print "You have made USD %d!" % (usd_total)
    return usd_total


def total_in_cad(orders):
    """This function calculates the total in CAD dollars ONLY if the currency for all the items is in CAD"""

    # Need to check if all prices are in Canadian
    currency = re.findall('"currency":"(.+?)"', orders, flags=0)
    filtered = [val for val in currency if val == "CAD"]

    # Calculate total if all prices in CAD
    if len(filtered) == len(currency):
        prices = re.findall('"total_price":"(.*?)"', orders, flags=0)
        cad_total = get_total(prices)
        print "You have made CAD %d!" % (cad_total)
        print "YAY!"
    else:
        print "Sorry cannot display CAD value as all the sales are not in CAD :( "

    return cad_total


def get_total(price_list):
    """This function calculates the total of the numbers given"""
    total = 0
    for price in price_list:
        # convert the string value to float
        price_num = float(price)
        total += price_num
    return total

def money_made():
    url = "https://shopicruit.myshopify.com/admin/orders.json?page=1&access_token=c32313df0d0ef512ca64d5b336a0d7c6"

    # use urllib to fetch and open the url
    try:
        socket = urllib2.urlopen(url)
        text = socket.read()

        usd_total = total_in_usd(text)
        cad_total = total_in_cad(text)

    except URLError as e:
        print 'Could not reach the server'
        print 'Error: ', e.reason

    return cad_total


if __name__ == "__main__":

    url = "https://shopicruit.myshopify.com/admin/orders.json?page=1&access_token=c32313df0d0ef512ca64d5b336a0d7c6"

