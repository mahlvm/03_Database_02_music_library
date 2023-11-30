from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# #Print ALL rows
# album_repository = AlbumRepository(connection)
# albums = album_repository.all()
# for album in albums:
#     print(album)

# #Print just the choos row
# print (album_repository.find(1))

from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!" 
            "What would you like to do?"
            "1 - List all albums"
            "2 - List all artists"

)
        x = input()
        print("Enter your choice:" + x)

    

#     artist_repository = ArtistRepository(self._connection)
#     artists = artist_repository.all()

#     for artist in artists:
#         print(f"{artist.id}: {artist.name} ({artist.genre})")

if __name__ == '__main__':
    app = Application()
    app.run()