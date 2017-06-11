from django import template

register = template.Library()

@register.filter(name='mult')
def mult( value, arg ) :
    print( value )
    print( arg )
    return ( float( value ) * float( arg ) )