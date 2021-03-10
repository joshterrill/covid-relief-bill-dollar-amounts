# COVID Relief Bill Money

This repository attempts to parse the December 21, 2020 COVID relief bill, looking for references to dollar amounts spent and saving them to html files. Currently there are 2 html files, one containing sections of text that reference all dollar amounts (`referenced-dollars.html`), and another which references specific dollar amounts that are being given to outside-countries (`referenced-countries.html`).

The standalone script can be found in `script.py` and can be run via `python3 script.py`

This repository is the focus of a blog post I wrote on https://joshterrill.com called [*"Where does all the money go?"*](https://joshterrill.com)

A PDF hosted version of the original text can be found on the house website: https://rules.house.gov/sites/democrats.rules.house.gov/files/BILLS-116HR133SA-RCP-116-68.pdf

I found a mirror of the original PDF that had an option to download it as a .txt file here: https://beta.documentcloud.org/documents/20433222-bills-116hr133sa-rcp-116-68 - this is the file that was used and can be found in this repo called `bills-116hr133sa-rcp-116-68.txt`. 

If you come up with any other interesting things to extract/parse from this text, or would like to improve upon it, **pull requests are welcome.**