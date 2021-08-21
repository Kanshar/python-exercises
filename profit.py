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
        if datalen == 0:
            return 0
        max_profit = 0
        for ibuy in range(datalen-1):
            for isell in range(ibuy+1, datalen):
                if prices[ibuy] < prices[isell]:
                    profit = prices[isell] - prices[ibuy]
                    if profit > max_profit:
                        max_profit = profit
                        LOG.debug("cost=%f, sell=%f", prices[ibuy], prices[isell])
                        LOG.debug("max_profit (either intermediate or final)=%f", max_profit)
        return max_profit
    except (IndexError, TypeError) as expt:
        LOG.exception(expt)
        return -1


if __name__ == "__main__":
    LOG.setLevel(logging.DEBUG)
    stock_prices_yesterday = [10.2, 7.4, 5.5, 8.0, 11.1, 9.9]*10*24
    x = get_max_profit(stock_prices_yesterday)
    print(f"Max profit = {x}")
