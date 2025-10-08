from lib.track import Track

class MusicTracker:
    def __init__(self):
        self.tracklist = []

    def add_track(self, title, artist):
        track = Track(title, artist)
        self.tracklist.append(track)

    def list_tracks(self):
        return [f"{track.title} by {track.artist}" for track in self.tracklist]

    def list_unique_artists(self):
        return list(set([track.artist for track in self.tracklist]))
