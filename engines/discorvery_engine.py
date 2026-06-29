from hidden_gems.models.artist import Artist


class DiscoveryEngine:

    def __init__(self):

        self.artists = []

    def add(self, artist: Artist):

        self.artists.append(artist)

    def all(self):

        return self.artists