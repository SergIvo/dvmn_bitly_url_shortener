# Bitly Command Line URL Shortener

## About

This is a small command line tool based on free API of [Bitly URL shortener](https://bitly.com/). This tool accepts URL as an argument and make shorter link aliased to it. If bit.ly short link is provided as an argument, application tells how much times users clicked on this link.

This application created for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/)

## Running the application

1. Download application files from GitHub using `git clone` command:
```
git clone https://github.com/SergIvo/dvmn_bitly_url_shortener
```
2. Create virtual environment to avoid conflicts with other versions of the same packages. Using python [venv](https://docs.python.org/3/library/venv.html) library is recommended for this purpose:
```
python -m venv venv
```
Then install dependencies from "requirements.txt" in created virtual environment using `pip` package manager:
```
pip install -r requirements.txt
```
To run application, you should also have a Bitly API key set as an environment variable:
```
export BITLY_API_KEY="your Bitly API key"
```
Run `main.py` with a URL as an argument:
```
python main.py https://somethinglo.ng/wfjnekfjkejf3kjn3jn4k9ni
```
