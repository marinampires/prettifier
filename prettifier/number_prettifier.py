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
    integer = number/million
    mod = number % million
    if mod == 0:
        return "%dM" % integer
    else:
        return "%d.%dM" % (integer, mod)
    