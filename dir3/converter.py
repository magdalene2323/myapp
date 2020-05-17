def numinput(prompt): 
    value = str(input(prompt))
    try: 
        value = int(value)
        return value
    except ValueError: 
        try: 
            value = float(value)
            return value
        except:
            print('That\'s not a valid value. Please enter a numeric value. Try again.') 
            return ''


def Converter():
    dictionary ={
    0:['metres','m'], 1:['feet','ft'], 2:['celcius','C'], 
    3:['farenheit','F'], 4:['kilograms','kg'], 5:['pounds','Ib']
}
    list1 = ['A','B','C','D','E','F']
    conversion = input('Specify the conversion you want: ')
    conversion = conversion.upper()
    if conversion == 'QUIT': 
        print('Thank you for using the converted. See you again.')
    elif conversion == 'A' or conversion == 'B' or conversion =='C' or conversion =='D' or conversion =='E' or conversion=='F':
        index = list1.index(conversion)
        value = numinput(f'Enter a value in {dictionary[index][0]}: ')
        if value == '':
            return Converter()
        else: 
            if conversion == 'A': 
                new_value = value*3.281
            elif conversion == 'B': 
                new_value = value/3.281
            elif conversion == 'C': 
                new_value = (value*9/5)+32
            elif conversion == 'D': 
                new_value = (value-32)*5/9
            elif conversion == 'E': 
                new_value = value*2.205
            elif conversion == 'F': 
                new_value = value/2.205
            if index%2 == 0: 
                print(f'{value} {dictionary[index][1]} = {new_value:.2f} {dictionary[index+1][1]}')
            else: 
                print(f'{value} {dictionary[index][1]} = {new_value:.2f} {dictionary[index-1][1]}')
            return Converter()
    else: 
        print('Invalid selection. Please specify a conversion between A-F.')
        return Converter()


Converter()