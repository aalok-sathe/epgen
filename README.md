# epgen.py

[![made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### A random episode generator for your favorite binge watching show

### Installation

#### from source:
Install the requisite package(s)


    python3 -m pip install --upgrade [--user] tvdb_api argparse requests

Obtain `epgen.py`

    git clone [the/URL/of/this/repository.git]
    cd epgen

#### pyPI:
coming soon

### Usage (example)

    $ python3 epgen.py name_of_show [-s SEASONS] [-e EPISODES] [-h] [-i]

- `name_of_show` (required): the approximate name of show to
look up in the database.
    * example: `python3 epgen.py`
- `-s, --seasons SEASONS` (optional): a whitespace-separated list of season
numbers to randomly choose from
    * example: `python3 epgen.py -s 4 8 9`
- `-e, --episodes EPISODES` (optional): a whitespace-separated list of
integers representing particular episode numbers to randomly
choose from
    * example: `python3 epgen.py -s 9 -e 16 17 18 19`
- `-h`, `--help` (optional): show a usage help message
- `-i`, `--include-extras` (optional): whether to include a season 0 in the random selection, i.e., most commonly, the season of bloopers or extras footage
- `-d`, `--description` (optional): display a brief summary of the episode that was chosen

Example usage:

    $   python3 epgen.py the office us
    ::  Season 8 Episode 2 of The Office (US) : 'The Incentive'

    $   python3 epgen.py the good place -s 1 2 -e 2 3 4
    ::  Season 1 Episode 2 of The Good Place : 'Flying'

    $   python3 epgen.py the office us -i
    ::  Season 0 Episode 14 of The Office (US) : 'The Office Retrospective'

    $   python3 epgen.py sacred games --desc
    ::  Season 1 Episode 2 of Sacred Games : 'Halahala'
    ::  News of Ganesh Gaitonde creates a stir among Mumbai's VIPs, from politicians to film stars. Removed from the case, Sartaj begins his own investigation.

### Future features and bugfixes
- [x] Pass list of seasons as argument to select episodes from
- [x] Weigh random choice by the number of episodes in each season
- Create web interface
- Support to install script in system path so you can call `epgen` from anywhere
- [moonshot] Exclude episodes with major plot points
