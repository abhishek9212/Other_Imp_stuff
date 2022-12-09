def convert(celsius):
    fahrenheit = ((9/5)*celsius) + 32
    return fahrenheit

temp = int(input("enter temperature in Celsius: "))

tempFahrenheit = convert(temp)
print("The temperature in fahrenheit is: ", str(tempFahrenheit) + " F")