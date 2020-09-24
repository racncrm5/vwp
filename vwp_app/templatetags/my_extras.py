from django import template

register = template.Library()

@register.filter(name='remove_str')
def remove_str(value,arg):
    """
    This removes out all values of "arg" from the string
    """
    return value.replace(arg,'')

# register.filter('remove_str',remove_str)
