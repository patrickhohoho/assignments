def digits2letters(digits):
    digits = str(digits)
    def loopProcessing(index, string, result):
        if index == len(digits):
            result.append(string)
            return
        for letter in dict[digits[index]]:
            loopProcessing(index+1, string+letter, result)

    dict = {'0':[''],
            '1':[''],
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
            }
    result = []
    loopProcessing(0, '', result)
    print("Possible letters are:", result)
    return result

digits = input("Input your digits to convert to letters: ")
while True:
    if digits.isdigit():
        break
    else:
        digits = input("Please input only digits: ")

digits2letters(digits)