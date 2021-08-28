#!/usr/bin/env python3
"""
Optimize profits
"""
import logging
from time import time

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

def timing(func):
    """Print time taken to execute func()
    """
    def wrap(*args):
        tstart = time()
        result = func(*args)
        tend = time()
        diff = tend - tstart
        LOG.info("%s, args: [%s] = {%f}, elapsed: {%f} sec",
            func.__name__, args, result, diff)
        return result
    return wrap

@timing
def get_max_profit(prices):
    """Get the max profit possible from a list of prices with only 1 buy
        and 1 sale
            Parameters:
                prices : list of prices (int[] or float[])
            Returns:
                max possible profit (int or float)
    """
    LOG.debug("Called get_max_profit")
    try:
        datalen = len(prices)
        if datalen == 0 or datalen == 1:
            return 0
        max_profit = 0
        low, high = prices[0], 0
        for i in range(1, datalen):
            if prices[i] < low:
                low, high = prices[i], 0
            elif prices[i] > high:
                high = prices[i]
            profit = high - low
            if profit > max_profit:
                max_profit = profit
        return max_profit
    except (IndexError, TypeError) as expt:
        LOG.exception(expt)
        return -1


if __name__ == "__main__":
    LOG.setLevel(logging.DEBUG)
    stock_prices_yesterday = [9, 10, 3, 5, 4, 4, 9, 9, 7, 7, 8, 7, 5, 7]
    x = get_max_profit(stock_prices_yesterday)
    print(f"max_profit = {x}" )
