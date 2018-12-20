import random # to randomize the episode
import tvdb_api # to retrieve the name and the number of episodes of a show
import sys # to log error to stderr

shows = tvdb_api.Tvdb()


class EpisodeRandomizer:
    def __init__(self, showname=None, season=None, episode=None):
        if season is not None or episode is not None:
            raise NotImplementedError
        self.tvdb = tvdb_api.Tvdb()
        try:
            print("INFO: looking for show information", file=sys.stderr)
            self.show = self.tvdb[showname]
        except tvdb_api.tvdb_shownotfound as error:
            print("ERR: no such TV show: {}".format(showname), file=sys.stderr)
            raise SystemExit

    def get_numseasons(self):
        self.numseasons = 0
        for season in self.show:
            if season:
                self.numseasons += 1
        return self.numseasons

    def get_numepisodes(self, season):
        numepisodes = 0
        for episode in self.show[season]:
            numepisodes += 1
        return numepisodes

    def get_season(self, exclude=None):
        if exclude is not None:
            raise NotImplementedError
        if not hasattr(self, 'numseasons'):
            self.numseasons = self.get_numseasons()
        return random.randint(1, self.numseasons)

    def get_episode(self, season, exclude=None):
        if exclude is not None:
            raise NotImplementedError
        return random.randint(1, self.get_numepisodes(season))

    def get_random_ep(self):
        season = self.get_season()
        episode = self.get_episode(season)
        return season, episode

    def print_random_episode(self):
        result = self.get_random_ep()
        # print("The Random Generator says:")
        print("Season {} Episode {} of {}".format(*result,
                                                  self.show['seriesName']))
        return result
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python epgen.py [name_of_show]")
        raise SystemExit
    randomizer = EpisodeRandomizer(" ".join(sys.argv[1:]))
    randomizer.print_random_episode()
