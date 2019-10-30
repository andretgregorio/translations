from classes.Locale import Locale
from classes.Value import Value
from classes.Translation import Translation


class TranslationsOps(object):
    @classmethod
    def create(cls, data_frame, desired_locales, translation_status):
        translations = []
        for i, row in data_frame.iterrows():
            r = row.to_dict()
            feature = r['Unnamed: 2']
            key = r['Unnamed: 3']
            values = row[4:].to_dict()
            for l, v in values.items():
                locale = Locale(l)
                value = Value(v, values[locale.fallback])
                if locale.main in desired_locales:
                    translations.append(Translation.factory(key, feature, value.get(), locale.get(), translation_status))
        return translations