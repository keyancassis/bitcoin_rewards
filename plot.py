import pandas as pd
import sys
import os

BLOCKS_PER_HALVING = 210000
BITCOIN_DATA_FILE = 'data/block_subsidy.csv'

def main():
    print(pd)
    print(os.listdir('data'))
    print(os.path.isfile('data/block_subsidy.csv'))

    try:
        df = pd.import_csv(BITCOIN_DATA_FILE)
    except Exception as err:
        print(f'Failed to load {BITCOIN_DATA_FILE}. Error: {err}.')
        sys.exit(0)
    print(df)




if __name__ == '__main__':
    main()
