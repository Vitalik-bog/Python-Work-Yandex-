def numberInEnglish(number):
    first = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
    second = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
    tens = ('ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    if len(str(number)) == 3:
        data, res = (int(str(number)[0]), int(str(number)[1]), int(str(number)[2])), ''
        res += first[data[0]-1] + ' hundred'
        if data[1] != 0 or data[2] != 0: res += ' and'
        if data[1] == 1: res += ' ' + second[data[2]]
        else:
            if data[1] != 0: res += ' ' + tens[data[1]-1]
            if data[2] != 0: res += ' ' + first[data[2]-1]        
        return res
    elif len(str(number)) == 2:
        data, res = (int(str(number)[0]), int(str(number)[1])), ''
        if data[0] == 1: res += second[data[1]]
        else:
            res += tens[data[0]-1]
            if data[1] != 0: res += ' ' + first[data[1]-1]
        return res
    elif len(str(number)) == 1:
        if number == 0: return 'zero'
        res = first[number-1]
        return res