from lib.album import Album

def test_contructs_with_field():
    album = Album(1, "Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == 1995
    assert album.album_id == 2

        