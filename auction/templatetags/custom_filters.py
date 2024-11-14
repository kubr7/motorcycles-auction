# your_app/templatetags/custom_filters.py
from django import template

register = template.Library()


@register.filter
def format_number(number):
    # Convert the number to a string and reverse it for easier processing
    num_str = str(number)[::-1]

    # Initialize an empty list to hold the parts of the number
    parts = []

    # Process the first group of 3 digits
    parts.append(num_str[:3])

    # Process the rest of the number in groups of 2 digits
    for i in range(3, len(num_str), 2):
        parts.append(num_str[i : i + 2])

    # Join the parts with commas and reverse the result back to the original order
    formatted_number = ",".join(parts)[::-1]

    return formatted_number


@register.filter
def subtract(value, arg):
    return value - arg