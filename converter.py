def welcome(name):
    hi = "Hi "
    welcome = ",welcome to the Celsius to Farenheit converter. "
    return hi + name + welcome
    
print(welcome("hugo"))

def converter_2(celsius):
    celsius = input("Combien de degrés celsius ?")
    farenheit = (celsius * 9/5)+32   
    return (str(celsius) + "°C = " + str(farenheit) + "°F")

result = converter_2(21)
print(result)
