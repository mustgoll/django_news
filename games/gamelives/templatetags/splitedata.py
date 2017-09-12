from django import template


register=template.Library()

@register.simple_tag
def img_url(str,sp,wh):

    li=str.split(sp)
    if len(li)>=2:
        if wh=='left':
            return li[0]
        if wh=='right':
            return li[1]
    else:
        if wh=='left':
            return li[0]
        if wh=='right':
            return ''
