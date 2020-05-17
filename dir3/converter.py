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


def converter():
    global dictionary1
    conversion = input('Specify the conversion you want: ')
    conversion = conversion.upper()
    if conversion == 'QUIT': 
        print('Thank you for using the converted. See you again.')
    elif conversion in dictionary1:
        value = numinput(f'Enter a value in {dictionary1[conversion][0]}: ')
        if value == '':
            return converter()
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
            print(f'{value} {dictionary1[conversion][1]} = {new_value:.2f} {dictionary1[conversion][2]}')
            return converter()
    else: 
        print('Invalid selection. Please specify a conversion between A-F.')
        return converter()


dictionary1 = {
    'A':['metres','m','ft'],'B':['feet','ft','m'],'C':['celcius','C','F'], 'D':['farenheit','F','C'],
    'E':['kilograms','kg','Ibs'],'F':['pounds', 'Ibs','kg']
}
print('A: Metres to Feet \nB: Feet to Metres \nC: Celcius to Fahrenheit\nD: Farenheit to Celcius \nE: Kilograms to Pounds \nF: Pounds to Kilograms')
converter()

