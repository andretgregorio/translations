class Locale:
    def __init__(self, locale):
        self.main = set_locale(locale)
        self.fallback = get_fallback_locale(locale)
    
    def get(self):
        if str(self.main) != 'nan' and self.main != None:
            return self.main
        else:
            return self.fallback

    
def set_locale(locale):
    if locale == 'es_ES':
        return 'es'
    elif locale == 'es':
        return None
    elif locale == 'pt_BR':
        return 'pt'
    elif locale == 'pt':
        return None
    else:
        return locale

def get_fallback_locale(locale):
    english_locales = ['en_US', 'en_GB', 'en_IE']
    spanish_locales = ['es_AR', 'es_CL', 'es_MX', 'es_ES']
    portuguese_locales = ['pt_BR', 'pt_PT']

    if locale in english_locales:
        return 'en'
    elif locale in spanish_locales:
        return 'es'
    elif locale in portuguese_locales:
        return 'pt_BR'
    return locale