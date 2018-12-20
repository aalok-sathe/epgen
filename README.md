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

    $ python3 epgen.py name_of_show [-s SEASONS] [-e EPISODES] [-h]

- `name_of_show` (required): the approximate name of show to
look up in the database.
    * example: `python3 epgen.py`
- `-s SEASONS` (optional): a whitespace-separated list of season
numbers to randomly choose from
    * example: `python3 epgen.py -s 4 8 9`
- `-e EPISODES` (optional): a whitespace-separated list of
integers representing particular episode numbers to randomly
choose from
    * example: `python3 epgen.py -s 9 -e 16 17 18 19`
- `-h` (optional): show a usage help message

So a command like this would choose any arbitrary episode from
all episodes:

    $ python3 epgen.py the office us
    [example output] Season 9 Episode 15 of The Office (US)



### Future features and bugfixes
- Pass a particular season as commandline argument to select episodes from
- Weigh by the number of episodes a season has to make unbiased choice
- Create web interface
- Support to install script in system path so you can call `epgen` from anywhere
- [moonshot] Exclude episodes with major plot points
