import time
import sys
import logging

import click

from airswap_exercise import config
from airswap_exercise import connector


@click.group()
@click.option('-v', '--verbose', is_flag=True, default=False, help='Turn on debugging')
@click.pass_context
def cli(ctx, verbose):
    if verbose:
        level = logging.DEBUG
    else:
        level=logging.WARN
    logging.basicConfig(level=level)
    logging.debug('Start application')

@cli.command()
@click.pass_context
@click.option('-s', '--symbol', nargs=1, default=config.BASE_SYMBOL, help='Symbol to Get')
@click.option('-t', '--duration', nargs=1, default=60, help='Same size in seconds')
def calculate_mean(ctx, symbol, duration):
    logging.debug("Calculating Mean")

    current_sum = 0.0
    number_of_samples = 0
    seconds = 0

    while True:
        try:
            if seconds == duration:
                print "Mean for %s over %d second sample: %s" % (symbol, duration, 
                    str(current_sum / number_of_samples))
                number_of_samples = 0
                current_sum = 0.0
                seconds = 0
            try:
                res = connector.get_price(symbol)
                current_sum += res
                number_of_samples += 1
            except ValueError:
                break
            except Exception as e:
                print e

            seconds += 1
            time.sleep(1)

        except Exception as e:
            print e
            break





    

