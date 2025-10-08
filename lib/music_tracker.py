from lib.track import Track

class MusicTracker:
    def __init__(self):
        self.tracklist = []

    def add_track(self, track):
        self.tracklist.append(track)

    def list_tracks(self):
        return self.tracklist
