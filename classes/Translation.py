class Translation:
    def __init__(self, feature, key, value, locale, translation_status):
        self.feature = feature
        self.key = key
        self.value = value
        self.locale = locale
        self.translation_status = translation_status

    @classmethod
    def factory(cls, feature, key, value, locale, translation_status):
        if feature and key and value and locale:
            return Translation(feature, key, value, locale, translation_status)
        else:
            print(f'[WARNING] No query created for paramters feature: "{feature}", key: "{locale}, value: "{value}, locale: "{locale}')