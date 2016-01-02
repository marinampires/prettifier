million = 1000000
def prettifier(number):
    if isinstance(number, (int, long, float)):
        if number < million:
            return number
        number_prettified = ""
        
        if number_is_million(number):
          return  convert_to_million(number)
        return number_prettified
    else:
        raise ValueError('The type is not a numeric value') 

def number_is_million(number):        
    return number/million > 0

def convert_to_million(number):
    div = divmod(number,million)
    if div[1] == 0:
        return "%dM" % div[0]
    else:
        return "%d.%sM" % (div[0], str(div[1])[0])
    