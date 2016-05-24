"""
print("Temperature Conversion program")

celsiusValue = (float(input("Enter temperature in celsius:")))
fahrenheitValue= celsiusValue * 9 / 5 + 32
kelvinValue= celsiusValue + 273
print("celcius value:", celsiusValue)
print("fahrenhiet value:", fahrenheitValue)
print("kelvin value:", kelvinValue)
"""
def get_celsius():
    celcius = int(input("Enter temperature in celcius: "))
    return celcius

def main():
    celcius=get_celsius()
    fahrenheit= celcius * 9 / 5 + 32
    print("celcius:", celcius)
    print("fahrenhiet:", fahrenheit)

main()