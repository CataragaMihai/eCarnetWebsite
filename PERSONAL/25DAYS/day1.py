# Temperature Converter day 1 project

FAHRENHEIT_TO_CELSIUS = 5/9
CELSIUS_TO_FAHRENHEIT = 9/5 
OFFSET = 32

# User input

celsius_input = float(input("Write down the tempereture in C to convert in F: "))
fahrenheit_input = float(input("Write down the tempereture in F to convert in C: "))

# Conversions 

converted_to_f = (celsius_input * CELSIUS_TO_FAHRENHEIT) + OFFSET
converted_to_c = (fahrenheit_input - OFFSET) * FAHRENHEIT_TO_CELSIUS

#Display 

print(f"{celsius_input}C --> {converted_to_f:.1f}F") 
print(f"{fahrenheit_input}F --> {converted_to_c:.1f}C")

