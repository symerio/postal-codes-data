This repository is a mirror of the [Geonames postal code datasets](http://download.geonames.org/export/zip/), provided for availability reasons. It was created as the the original location can periodically return 404 errors for [pgeocode](https://github.com/symerio/pgeocode) users.


### Sync scripts

To synchronize the `data/` folder locally with the origin, install Python 3.7+ and run,
```
pip install -r requirements.txt
python scripts/01_sync_data.py
```

### License

Postal code datasets are re-distributed with the same [Creative Commons Attribution 4.0 license](https://creativecommons.org/licenses/by/4.0/) as the original files.

Code in this repository is distributed with the [Appache-2.0 license](http://www.apache.org/licenses/LICENSE-2.0.html).
