# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them

from lib.music_tracker import MusicTracker

def test_music_tracker_instantiates_with_tracklist_attribute():
    mt = MusicTracker()
    assert mt.tracklist == []

def test_add_track_adds_track_to_tracklist():
    mt = MusicTracker()
    mt.add_track("Waterloo by ABBA")
    assert mt.tracklist == ["Waterloo by ABBA"]

def test_list_tracks_returns_single_track():
    mt = MusicTracker()
    mt.add_track("Waterloo by ABBA")
    assert mt.list_tracks() == ["Waterloo by ABBA"]

def test_list_tracks_returns_two_tracks():
    mt = MusicTracker()
    mt.add_track("Waterloo by ABBA")
    mt.add_track("Money Money Money by ABBA")
    assert mt.list_tracks() == [
        "Waterloo by ABBA",
        "Money Money Money by ABBA"
    ]

