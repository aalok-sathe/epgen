import random # to randomize the episode
import tvdb_api # to retrieve the name and the number of episodes of a show
import sys # to log error to stderr
import argparse
from requests.exceptions import ConnectionError


class EpisodeRandomizer:
    def __init__(self, showname=None, season=None, episode=None):
        """
        Contructor
        instantiates a randomizer instance
        ---
        showname -> str: the approximate name of the show
        season -> int: the specific season to limit to (default: None)
        episode -> int: a specific episode (from all seasons unless specified)
                        to limit randomization to (default: None)
        """
        print(showname, season, episode)
        self.season, self.episode = season, episode
        self.tvdb = tvdb_api.Tvdb()
        try:
            # print("INFO: looking for show information", file=sys.stderr)
            self.show = self.tvdb[showname]
        except tvdb_api.tvdb_shownotfound as error:
            print("ERR: no such TV show: {}".format(showname), file=sys.stderr)
            raise SystemExit
        except ConnectionError as error:
            print("ERR: please check your network connection", file=sys.stderr)
            raise SystemExit

    def get_numseasons(self):
        """
        get_numseasons
        return the number of seasons a TV show has
        ---
        """
        self.numseasons = 0
        for season in self.show:
            if season:
                self.numseasons += 1
        return self.numseasons

    def get_numepisodes(self, season):
        """
        get_numepisodes
        return the number of episodes in a particular season
        ---
        """
        numepisodes = 0
        for episode in self.show[season]:
            numepisodes += 1
        return numepisodes

    def get_season(self, exclude=None):
        """
        get_season
        randomly pick a season or return the one the user asked for
        ---
        """
        if exclude is not None:
            raise NotImplementedError
        if self.season is not None: # user requested a particular season
            return self.season
        if not hasattr(self, 'numseasons'): # run only once
            self.numseasons = self.get_numseasons()
        return random.randint(1, self.numseasons)

    def get_episode(self, season, exclude=None):
        """
        get_episode
        randomly pick an episode from a particular season or return the one
        the user specifically requested
        ---
        """
        if exclude is not None:
            raise NotImplementedError
        if self.episode is not None: # user requested a particular episode num
            return self.episode
        return random.randint(1, self.get_numepisodes(season))

    def get_random_ep(self): # the star method of the class
        """
        get_random_ep
        knowing the number of seasons and number of episodes, pick a random
        from both and return the pair
        ---
        """
        season = self.get_season()
        episode = self.get_episode(season)
        return season, episode

    def print_random_episode(self): # pretty-print the output of the randomizer
        """
        print_random_episode
        just a helper to nicely output result of randomization
        ---
        """
        result = self.get_random_ep()
        # print("The Random Generator says:")
        print("Season {:d} Episode {:d} of {}".format(*result,
                                                      self.show['seriesName']))
        return result # also return it, just in case it's needed for sth else

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
    config = parser.parse_args()
    print(config)
    randomizer = EpisodeRandomizer(' '.join(config.name), season=config.season,
                                   episode=config.episode)
    random = randomizer.print_random_episode()
