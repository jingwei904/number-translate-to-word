def say(number) -> str:
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    megaunit = {1_000_000_000: ' billion', 1_000_000: ' million', 1_000: ' thousand', 1: ''}

    result = ''

    for value in megaunit.keys():
        if number // value >= 1:
            temp_number = number // value
            number = number % value
            word = write_number(temp_number)
            result = f"{result} {word}{megaunit[value]}" if result else f"{word}{megaunit[value]}"
    if result == '':
        return 'zero'
    else:
        return result

def write_number(number) -> str:
    result = ''
    num_to_word = {0: '' , 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}
    special_prefix = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 80: 'eighty'}

    if number // 100 >= 1:
        result = num_to_word[number // 100] + ' hundred'
        number = number % 100

    if number == 0:
        return result
    elif number <= 12:
        word = num_to_word[number]
        result = f"{result} {word}" if result else word
    elif number in [13, 15]:
        word = "thirteen" if number == 13 else "fifteen"
        result = f"{result} {word}" if result else word
    elif number <= 19:
        word = num_to_word[number%10] + 'teen'
        result = f"{result} {word}" if result else word
    elif number <= 59 or (number >= 80 and number <= 89):
        prefix = special_prefix[(number//10) * 10]
        word = f"{prefix}-{num_to_word[number%10]}" if number%10!=0 else prefix
        result = f"{result} {word}" if result else word
    else:
        suffix = "ty-" if number%10!=0 else "ty"
        word = num_to_word[number//10] + suffix + num_to_word[number%10]
        result = f"{result} {word}" if result else word
        
    return result
    
        