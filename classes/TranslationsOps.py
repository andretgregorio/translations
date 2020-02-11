from classes.Locale import Locale
from classes.Value import Value
from classes.Translation import Translation


class TranslationsOps(object):
    @classmethod
    def create(cls, data_frame, desired_locales, translation_status):
        translations = []
        for i, row in data_frame.iterrows():
            r = row.to_dict()
            feature = r['Unnamed: 1']
            key = r['Unnamed: 2']
            values = row[3:].to_dict()
            for l, v in values.items():
                locale = Locale(l)
                value = Value(v, values[locale.fallback])
                if locale.get() in desired_locales:
                    translations.append(
                        Translation.factory(feature, key, value.get(), locale.get(), translation_status))
        return translations