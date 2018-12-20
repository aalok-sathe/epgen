# epgen.py

[![made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### A random episode generator for your favorite binge watching show

### Installation

#### from source:
- Install the requisite package(s)


    $ python3 -m pip install --upgrade [--user] tvdb_api argparse requests

- Obtain `epgen.py`


    $ git clone [the/URL/of/this/repository.git]
    $ cd epgen

#### pyPI:
coming soon

### Usage (example)
Choose any arbitrary episode

    $ python3 epgen.py the office us
    [example output] Season 9 Episode 15 of The Office (US)

### Future features and bugfixes
- Pass a particular season as commandline argument to select episodes from
- Weigh by the number of episodes a season has to make unbiased choice
- Create web interface
- [moonshot] Exclude episodes with major plot points
