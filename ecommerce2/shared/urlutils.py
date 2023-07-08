
azen_eq={'ü':'u','ş':'sh','ö':'o','ğ':'gh','ı':'i','ə':'e','ç':'ch',
        'Ü':'CH','Ş':'SH', 'Ö':'O','Ğ':'GH','İ':'I','Ə':'E','Ç':'CH',
}

def get_slug(text):
    result = ''
    for letter in text:
        if letter.isalnum():
            result += azen_eq.get(letter,letter)
        elif letter == ' ':
            result += '-'
    return result