print('Welcome to the Convertor!')
Type=input('Would you like to convert Temperture, Money, Measurements, or Time?')
if(Type in 'Temperture'):
    print('What type of Temperture would you like to convert?')
if(Type in 'Money'):
    print('What type of Currency would you like to convert?')
    Money1=input('US Dollar, euro, Japanese yen, Australian dollar, Canadian dollar, and British pound')
    if(Money1 in 'US dollar'):
        print('What kind of Currency are converting to?')
        Money2=input('euro, Japanese yen, Australian dollar, Canadian dollar, or British pound')
        if(Money2 in 'euro'):
            Money3=input('Insert the money needed.')
            Money4=(Money3 * 99.88)
            print(Money4)
if(Type in 'Measurements'):
    print('What Measurements would you like to convert?')
if(Type in 'Time'):
    print('How much time would you like to convert?')
