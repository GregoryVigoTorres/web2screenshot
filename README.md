#web2screenshot

**web2screenshot** is a Scrapy and scrapy-splash crawler that follows all the local links it can find for a website and saves a screenshot of every page.


##Installation
Requires Python 3
It's been tested using 3.5 and 3.6, but other Python 3 versions will probably work.

Install Python dependencies: `pip install -r requirements.txt`
It's recommended to use a virtual env e.g. `pyvenv venv` or something like `python3.6 -m venv venv`.

[Docker](https://www.docker.com/) is strongly recommended.


##Usage
If you want to use the `runsplash` script you need to have [Docker](https://www.docker.com/) installed.
I think this is by far the easiest way to run splash, but it's not the only way.
You may need to make runsplash executable. e.g. `chmod 755 runsplash`

If you don't use the `runsplash` script, be sure to verify the Splash options in `settings.py`. Consult the [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash) docs for reference.

This spider is run like a standard [Scrapy spider](https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy-spider) with `scrapy crawl shoot`.

Define you start URLs in `spiders/shoot.py`.

Relevant settings are in the standard Scrapy settings file. The most relevant options are:
`SPLASH_ARGS` - See the [Splash docs](https://splash.readthedocs.io/en/stable/) for reference. The only things you probably want to change here are `quality`, `timeout` or `wait`.
`DATA_DIR` - This is where your screenshots will be saved


Copyright Gregory Vigo Torres, 2017
License GPL v.3
