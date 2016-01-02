million = 1000000
def prettifier(number):
    if isinstance(number, (int, long, float)):
        if number < million:
            return number
        number_prettified = ""
        
        return number_prettified
    else:
        raise ValueError('The type is not a numeric value') 
