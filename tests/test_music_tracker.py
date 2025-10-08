# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them

from lib.music_tracker import MusicTracker
from lib.track import Track

def test_music_tracker_instantiates_with_tracklist_attribute():
    mt = MusicTracker()
    assert mt.tracklist == []

def test_add_track_adds_track_to_tracklist():
    mt = MusicTracker()
    mt.add_track("Waterloo", "ABBA")
    assert mt.tracklist[0].title == "Waterloo"
    assert mt.tracklist[0].artist == "ABBA"

def test_list_tracks_returns_single_track():
    mt = MusicTracker()
    mt.add_track("Waterloo", "ABBA")
    assert mt.list_tracks() == ["Waterloo by ABBA"]

def test_list_tracks_returns_two_tracks():
    mt = MusicTracker()
    mt.add_track("Waterloo", "ABBA")
    mt.add_track("Money Money Money", "ABBA")
    assert mt.list_tracks() == [
        "Waterloo by ABBA",
        "Money Money Money by ABBA"
    ]

def test_list_artists_returns_two_artists():
    mt = MusicTracker()
    mt.add_track("Waterloo", "ABBA")
    mt.add_track("Money Money Money", "ABBA")
    mt.add_track("Comfortably Numb", "Pink Floyd")
    assert sorted(mt.list_unique_artists()) == [
        "ABBA",
        "Pink Floyd"
    ]

