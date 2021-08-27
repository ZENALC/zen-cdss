"""
Tool to scrape province, district, and municipality information in Nepal.
"""

import json
import ssl

import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context  # noqa - This is required for SSL in OS-X.
URL = 'https://www.nepalgov.com/list-of-municipalities-and-rural-municipalities-english/'
FILE_NAME = 'nepal_map.json'


def main():
    """
    Main tool to scrape Nepalese map information.
    """
    # Initialize a dataframe with province/district/municipality information from the URL above.
    df = pd.read_html(URL)[0]

    # Make the provinces a bit more clear.
    df.Province = df.Province.str.replace('1', 'Province No. 1')
    df.Province = df.Province.str.replace('2', 'Province No. 2')
    df.Province = df.Province.str.replace('5', 'Lumbini Province')

    # Add "Province" to end of each province if it doesn't already contain the word "Province".
    df.Province = df.Province.apply(lambda x: f'{x} Province' if 'Province' not in x else x)

    # Convert DF to a dictionary for easier parsing.
    df_dict = df.to_dict(orient='records')

    # Create dictionary with province as the main key, district as sub-key, and municipalities as the values.
    parsed_dict = {}
    for entry in df_dict:
        province = entry.pop('Province')
        district = entry.pop('District')

        parsed_dict.setdefault(province, {}).setdefault(district, []).append(entry.pop('Local Level Name'))

    # Dump result dictionary to file name specified.
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(parsed_dict, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
