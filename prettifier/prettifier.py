_MILLION = 1000000
_SHORT_SCALE = 1000
_SCALE_KEYS = {1: 'M', 2: 'B', 3: 'T'}   


def _is_number_prettifiable(number):
    # Check in the number greater than 6 digits
    return abs(number) >= _MILLION

def _has_number_decimal_part(remainder):
    return remainder != 0

def _should_get_next_short_scale(quotient, scale_key):
    #if the quotient is bigger than 1 and bigger than short scale, it tries the next scale and go on until reach the trillion scale
    return quotient > 0 and quotient >= _SHORT_SCALE and scale_key < _SCALE_KEYS.keys()[-1]

def _get_first_integer_remainder(remainder, scale):
    # use remainder/(scale/10) to get the first integer of remaider
    return remainder/(scale/10)

def prettify(number, scale=_MILLION, scale_key=1):
    if isinstance(number, (int, long, float)):
        
        if not(_is_number_prettifiable(number)):
            return number

        #Makes the division and gets the remainder
        quotient, remainder = divmod(number,scale)

        if _should_get_next_short_scale(quotient, scale_key):
            #
            return prettify(number, scale * _SHORT_SCALE, scale_key + 1)
        
        # Check if truncated number is not an integer
        if _has_number_decimal_part(remainder):
            
            return "%d.%d%s" % (quotient, _get_first_integer_remainder(remainder, scale), _SCALE_KEYS[scale_key])
        else:
            return "%d%s" % (quotient, _SCALE_KEYS[scale_key])
    else:
        raise ValueError('The type is not a numeric value') 
