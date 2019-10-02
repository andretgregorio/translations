from classes.Query import Query


class Translations(object):
    @classmethod
    def create(cls, data_frame):
        queries = []
        for i, row in data_frame.iterrows():
            r = row.to_dict()
            feature = r['Unnamed: 2']
            key = r['Unnamed: 3']
            values = row[4:].to_dict()
            for l, v in values.items():
                value = cls.sanitize_string(v)
                locale = cls.get_locale(l)
                if cls.empty(value) and not cls.empty(locale):
                    default_locale = cls.getDefaultLocale(locale)
                    try:
                        default_value = values[default_locale]
                        if not cls.empty(default_value):
                            value = cls.sanitize_string(default_value)
                    except:
                        print(f'[WARNING] No default value for locale {default_locale}')
                if not cls.empty(value) and not cls.empty(locale) and not cls.empty(key) and not cls.empty(feature):
                    queries.append(Query(key, feature, value, locale))
                else:
                    print(f'[WARNING] Query no instancieated for {value} at locale {locale}')
        return queries
    
    @classmethod
    def empty(cls, value):
        return str(value) == 'nan' or value == None
    
    @classmethod
    def getDefaultLocale(self, locale):
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
    
    @classmethod
    def sanitize_string(cls, text):
        return text.strip().replace("'", "''")
    
    @classmethod
    def get_locale(cls, locale):
        if locale == 'es_ES':
            return 'es'
        elif locale == 'es':
            return None
        else:
            return locale