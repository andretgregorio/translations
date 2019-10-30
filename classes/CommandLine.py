import argparse

class CommandLine:
    @classmethod
    def parse_arguments(cls):
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '-q', 
            '--query', 
            type=str, 
            default='update_value', 
            help="The type of transaction that will be writter. Accepted values: 'insert' or 'update'"
        )
        parser.add_argument(
            '-i', 
            '--initial-row', 
            type=int, 
            default=1, 
            help="Initial row to be included in the translation"
        )
        parser.add_argument(
            '-f', 
            '--final-row', 
            type=int, 
            help="Last row to be included in the translation"
        )
        parser.add_argument(
            '-l', 
            '--locales', 
            type=str, 
            default='pt,en,en_US,en_GB,en_IE,es,es_AR,es_CL,es_MX,es_ES,de,fr,it,nl,pt_PT', 
            help="Use it to specify the locales that should be included in the .sql output file. If you don't specify the locales, the genrated .sql file will contain queries for all locales in the file."
        )
        parser.add_argument(
            '-ts', 
            '--translation_status', 
            type=int, 
            default=10, 
            help="Use it to specify the translation_status on the output queries. If not specified it will default to 10."
        )

        return vars(parser.parse_args())