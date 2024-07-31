from django import template
register = template.Library()

@register.filter 
def replace_1(string):
    if string == "NO":
        return "Not Opted in"
    if string == "ONO":
        return "No Offers"
    if string == "OWO":
        return "With Offers"
    return "Placed"

