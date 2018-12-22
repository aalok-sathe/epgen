#!/usr/bin/env python3

import random # to randomize the episode
import tvdb_api # to retrieve the name and the number of episodes of a show
import sys # to log error to stderr
import argparse
from requests.exceptions import ConnectionError
from colors import *


class EpisodeRandomizer:
    def __init__(self, showname=None):
        """
        Contructor
        instantiates a randomizer instance
        ---
        showname -> str: the approximate name of the show
        season -> int: the specific season to limit to (default: None)
        episode -> int: a specific episode (from all seasons unless specified)
                        to limit randomization to (default: None)
        """
        # print(showname)
        self.tvdb = tvdb_api.Tvdb()
        try:
            # print("INFO: looking for show information", file=sys.stderr)
            self.show = self.tvdb[showname]
        except tvdb_api.tvdb_shownotfound as error:
            print("ERR: '{}' not found".format(showname), file=sys.stderr)
            raise SystemExit
        except ConnectionError as error:
            sys.stdout.write(BOLD+RED)
            print("ERR: please check your network connection", file=sys.stderr)
            raise SystemExit
        self.seasons = dict()
        for season in self.show:
            self.seasons[season] = self.show[season]

    def get_numseasons(self, extras=None):
        """
        get_numseasons
        return the number of seasons a TV show has
        ---
        """
        raise DeprecationWarning
        self.numseasons = 0
        for season in self.show:
            if season or extras is not None:
                self.seasons[season] = self.show[season]
        return self.numseasons

    def get_numepisodes(self, season):
        """
        get_numepisodes
        return the number of episodes in a particular season
        ---
        """
        raise DeprecationWarning
        return len(self.seasons[season])

    def get_season(self, extras=None):
        """
        get_season
        randomly pick a season or return the one the user asked for
        ---
        """
        raise DeprecationWarning
        if self.season is not None: # user requested a particular season
            return self.season
        if not hasattr(self, 'numseasons'): # run only once
            self.numseasons = self.get_numseasons()
        return random.randint(1, self.numseasons)

    def get_episode(self, season, episode=None):
        """
        get_episode
        randomly pick an episode from a particular season or return the one
        the user specifically requested
        ---
        """
        raise DeprecationWarning
        if exclude is not None:
            raise NotImplementedError
        if episode is not None: # user requested a particular episode num
            return episode
        return random.randint(1, self.get_numepisodes(season))

    def get_random_ep(self, season=None, episode=None, extras=None):
        """
        get_random_ep
        knowing the number of seasons and number of episodes, pick a random
        from both and return the pair
        ---
        """
        options = []
        for s in self.seasons:
            for e in self.seasons[s]:
                if extras is not None or s != 0:
                    if season is None or int(s) in season:
                        if episode is None or int(e) in episode:
                            options.append((s,e))
                # print("{:d}\t{:d}".format(s,e))
        # print(options)
        choice = random.randint(0, len(options)-1) # get true unbiased random
                                                   # otherwise seasons with
                                                   # more episodes get more
                                                   # representation
        return options[choice]
        # season = self.get_season(extras=extras)
        # episode = self.get_episode(season)
        # return season, episode

    def print_random_episode(self, season=None, episode=None, extras=None,
                             desc=None):
        """
        print_random_episode
        just a helper to nicely output result of randomization
        ---
        """
        result = self.get_random_ep(season=season, episode=episode,
                                    extras=extras)
        epobj = self.show[result[0]][result[1]]
        # print("The Random Generator says:")
        print("Season {:d} Episode {:d} of {}".format(*result,
                                                      self.show['seriesName']),
              ": '{}'".format(epobj['episodeName']))
        if desc is not None:
            print(epobj['overview'])
        return epobj # also return it, just in case it's needed for sth else

if __name__ == '__main__': # run the print method only if we're main
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='+', type=str, help='The name of the '
                                                          'show. Example: '
                                                          'python3 epgen.py '
                                                          '"the office us"',
                        metavar='showname')
    parser.add_argument('-s', '--season', nargs='+', type=int,
                        help='Select from only these specific seasons. '
                             'Example usage: -s 1 4 5 8',
                        default=None)
    parser.add_argument('-e', '--episode', nargs='+', type=int,
                        help='Select from only these numbered episodes. '
                             'Example usage: -e 17 18 19 20 21',
                        default=None)
    parser.add_argument('-i', '--include-extras', nargs='*',
                        help='If passed, allows choosing season 0 which, '
                             'for most shows, contains bloopers and such.',
                        default=None)
    parser.add_argument('-d', '--description', nargs='*',
                        help='If passed, shows episode summary',
                        default=None)
    config = parser.parse_args()
    # print(config)
    randomizer = EpisodeRandomizer(' '.join(config.name))
    randep = randomizer.print_random_episode(season=config.season,
                                             episode=config.episode,
                                             extras=config.include_extras,
                                             desc=config.description)
