import sys
import pandas as pd
from datetime import datetime
from classes.CommandLine import CommandLine
from classes.TranslationsOps import TranslationsOps
from classes.Query import Query

class main:
    cmdline_args = CommandLine.parse_arguments()

    transaction_type = cmdline_args['query']
    initial_row = cmdline_args['initial_row']
    final_row = cmdline_args['final_row']
    desired_locales = cmdline_args['locales'].split(',')
    translation_status = cmdline_args['translation_status']

    file = "translations.xlsx"

    df = pd.read_excel(
        file,
        sheet_name="Gympassport Translations",
        header=1,
        skiprows=range(2, initial_row),
        nrows=final_row - initial_row
    )
    translations = TranslationsOps.create(df, desired_locales, translation_status)

    today = datetime.now()
    date = today.strftime("%d%m%Y_%H%M%S")
    with open(f'queries_{date}.sql', 'w') as file:
        for translation in translations:
            query = Query(translation)
            file.write(f"{query.write(transaction_type)}\n")


if __name__ == '__main__':
    main()