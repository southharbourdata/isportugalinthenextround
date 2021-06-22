import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_live_score():
    """Returns live score of the matches in GROUP F on 23/06/2021 
    in the EURO football championship"""
    
    result = requests.get("https://www.bbc.com/sport/football/european-championship/scores-fixtures/2021-06-21")
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')

    table = soup.find_all("ul")
    results_table = table[-3]
    lists_matches = results_table.find_all("a")
    test_li = lists_matches[1]
    lists_test = test_li.find_all("span")

    df_results = pd.DataFrame(columns=["home_score","away_score","home_name","away_name"])
    
    for idx, l in enumerate(lists_matches):
        content = l.find_all("span")

        df_results.loc[idx,"home_score"] = content[5].text
        df_results.loc[idx,"away_score"] = content[12].text
        df_results.loc[idx,"home_name"] = content[1].find_all("abbr")[0].text
        df_results.loc[idx,"away_name"] = content[9].find_all("abbr")[0].text

    return df_results