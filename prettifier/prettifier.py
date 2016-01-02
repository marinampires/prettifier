#!/usr/bin/env python

from number_prettifier import MILLION, SHORT_SCALE, SCALE_KEYS

def prettify(number, scale=MILLION, scale_key=1):
    # Check if the input is a number
    if isinstance(number, (int, long, float)):
        # Check in the number greater than 6 digits
        if number < MILLION:
            return number

        #Makes the division and gets the remainder
        quotient, remainder = divmod(number,scale)

        #if the quotient is bigget than 1 and bigger than short scale, it tries the next scale and go on until reach trillion scale
        if quotient > 0 and quotient >= SHORT_SCALE and scale_key < 3:
            return prettify(number, scale * SHORT_SCALE, scale_key + 1)
        
        # Check if there is a decimal value
        if remainder == 0:
            return "%d%s" % (quotient, SCALE_KEYS[scale_key])
        else:
            # use remainder/(scale/10) to get the first integer of remaider
            return "%d.%d%s" % (quotient, remainder/(scale/10), SCALE_KEYS[scale_key])

    else:
        raise ValueError('The type is not a numeric value') 

