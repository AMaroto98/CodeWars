from src.FriendOrFoe import friend
import pytest


def test_friend():

    assert friend(["Ryan", "Kieran", "Mark",]) == ["Ryan", "Mark"]
    assert friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]) == ["Ryan"]
    assert friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]) == ["Jimm", "Cari", "aret"]