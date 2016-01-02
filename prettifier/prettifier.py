_MILLION = 1000000
_SHORT_SCALE = 1000
_SCALE_KEYS = {1: 'M', 2: 'B', 3: 'T'}   


def prettify(number, scale=_MILLION, scale_key=1):
    # Check if the input is a number
    if isinstance(number, (int, long, float)):
        # Check in the number greater than 6 digits
        if number < _MILLION:
            return number

        #Makes the division and gets the remainder
        quotient, remainder = divmod(number,scale)

        #if the quotient is bigget than 1 and bigger than short scale, it tries the next scale and go on until reach trillion scale
        if quotient > 0 and quotient >= _SHORT_SCALE and scale_key < 3:
            return prettify(number, scale * _SHORT_SCALE, scale_key + 1)
        
        # Check if there is a decimal value
        if remainder == 0:
            return "%d%s" % (quotient, _SCALE_KEYS[scale_key])
        else:
            # use remainder/(scale/10) to get the first integer of remaider
            return "%d.%d%s" % (quotient, remainder/(scale/10), _SCALE_KEYS[scale_key])

    else:
        raise ValueError('The type is not a numeric value') 
