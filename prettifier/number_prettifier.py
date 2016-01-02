million = 1000000
short_scale = 1000

def prettifier(number):
    if isinstance(number, (int, long, float)):
        if number < million:
            return number
        number_prettified = ""

        if number_is_trillion(number):
          return  convert_to_trillion(number)

        if number_is_billion(number):
          return  convert_to_billion(number)
        
        if number_is_million(number):
          return  convert_to_million(number)
        return number_prettified
    else:
        raise ValueError('The type is not a numeric value') 

def number_is_trillion(number):        
    return int(number/(million * short_scale * short_scale)) > 0

def convert_to_trillion(number):
    div = divmod(number,million * short_scale * short_scale)
    if div[1] == 0:
        return "%dT" % div[0]
    else:
        return "%d.%sT" % (div[0], str(div[1])[0])

def number_is_billion(number):        
    return int(number/(million * short_scale)) > 0

def convert_to_billion(number):
    div = divmod(number,million * short_scale)
    if div[1] == 0:
        return "%dB" % div[0]
    else:
        return "%d.%sB" % (div[0], str(div[1])[0])

def number_is_million(number):        
    return int(number/million) > 0

def convert_to_million(number):
    div = divmod(number,million)
    if div[1] == 0:
        return "%dM" % div[0]
    else:
        return "%d.%sM" % (div[0], str(div[1])[0])
    