# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from zipfile import ZipFile
from io import BytesIO
from pathlib import Path
import shutil

import requests

from bs4 import BeautifulSoup
import logging

logging.basicConfig(format="%(asctime)-15s %(message)s")
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

# %%
BASE_URL = "http://download.geonames.org/export/zip/"


def main():
    logger.info(f"Fetching list of datasets from {BASE_URL}")
    res = requests.get(BASE_URL)
    if not res.ok:
        return
    txt = res.content.decode("utf-8")
    links_all = BeautifulSoup(txt, "html.parser").findAll("a")

    datasets = [
        el["href"].replace(".zip", "")
        for el in links_all
        if el["href"].endswith(".zip")
    ]

    datasets = [el for el in datasets if el not in ["GB_full.csv", "allCountries"]]

    # %%
    logger.info("Syncing datasets:")
    for idx, name in enumerate(datasets):

        r = requests.get(f"{BASE_URL}{name}.zip", stream=True)
        if not r.ok:
            print(r.content)
            raise ValueError

        with ZipFile(BytesIO(r.content)) as zf:
            key = Path(name).with_suffix(".txt")
            with zf.open(str(key), "r") as fh_in:
                with open(f"./data/{key}", "wb") as fh_out:
                    shutil.copyfileobj(fh_in, fh_out)

        logger.info(f"  .. {idx+1:02}/{len(datasets)}: {name}")


if __name__ == "__main__":
    main()
