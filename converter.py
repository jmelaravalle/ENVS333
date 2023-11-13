#Homework 5 Functions

#1

def convert_degrees_to_decimal(degrees, minutes, seconds, direction):
    degrees = float(degrees)
    minutes = float(minutes)
    seconds = float(seconds)

    decimal = degrees + (minutes + seconds/60) / 60

    if direction in ['S', 'W']:
        decimal *= -1

    return decimal

#2

def convert_decimal_to_degrees(decimal):
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = (decimal - degrees - minutes/60) * 3600

    direction = 'E'
    if decimal < 0:
        direction = 'W'
        degrees = abs(degrees)

    return degrees, minutes, seconds, direction

#3

def convert_miles_to_feet(miles):
    feet_per_mile = 5280  # 1 mile = 5280 feet (now I won't forget)
    feet = miles * feet_per_mile
    return feet

#4

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#5 

def calculate_volume(length, width, thickness):
    # Volume = Length x Width x Thickness
    volume = length * width * thickness
    return volume