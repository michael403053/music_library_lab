import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("NWA")
artist_repository.save(artist1)
artist2 = Artist("Snoop Dogg")
artist_repository.save(artist2)

album1 = Album("Straight Outta Compton", "Rap", artist1)
album_repository.save(album1)
album2 = Album("Doggystyle", "Hip Hop", artist2)
album_repository.save(album2)
album3 = Album("The Last Meal", "Hip-Hop", artist2)
album_repository.save(album3)

found_artist = artist_repository.select(artist1.id)
print(found_artist)

albums_for_artist = artist_repository.albums(artist1)

all_artists = artist_repository.select_all()
print(all_artists)

all_albums = album_repository.select_all()
print(all_albums)

pdb.set_trace()