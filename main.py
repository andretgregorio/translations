import argparse, sys
import pandas as pd
from datetime import datetime
from classes.Translations import Translations

class main:
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--query', type=str, help="The type of transaction that will be writter. Accepted values: 'insert' or 'update'")
    parser.add_argument('-i', '--initial-row', type=int, help="Initial row to be included in the translation")
    parser.add_argument('-f', '--final-row', type=int, help="Last row to be included in the translation")

    cmdline_args = vars(parser.parse_args())
    # 
    transaction_type = cmdline_args['query']
    initial_row = cmdline_args['initial_row']
    final_row = cmdline_args['final_row']

    file = "translations.xlsx"

    df = pd.read_excel(
        file,
        header=1,
        skiprows=range(2, initial_row),
        nrows=final_row - initial_row
    )
    queries = Translations.create(df)

    today = datetime.now()
    date = today.strftime("%d%m%Y_%H%M%S")
    with open(f'queries_{date}.sql', 'w') as f:
        for query in queries:
            f.write(f"{query.write(transaction_type)}\n")


if __name__ == '__main__':
    main()