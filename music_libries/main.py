class Song:
    def __init__(self, name: str, long: int) -> None:
        self.name = name
        self.long = long

class Album:
    def __init__(self, name: str, date: str, song_list: list) -> None:
        self.name = name
        self.date = date
        self.song_list = song_list
    
    def add_song(self, song: Song) -> None:
        self.song_list.append(song)

class Artist:
    artists = list()
    def __init__(self, name: str, date: str, album_list: list) -> None:
        self.name = name
        self.date_brith = date
        self.album_list = album_list
        Artist.artists.append(self)

    def add_album(self, album: Album) -> None:
        self.album_list.append(album)

    def get_artists() -> list:
        return Artist.artists
    
class Playlist:
    def __init__(self, name: str, discription: str, playlist: list) -> None:
        self.name = name
        self.discription = discription
        self.playlist = playlist
    
    def add_song(self, song: Song) -> None:
        self.playlist.add(song)
    
    def add_album(self, album: Album) -> None:
        for song in album.song_list:
            self.playlist.append(song)
    
    def add_artist(self, artist: Artist) -> None:
        for album in artist.album_list:
            for song in album.song_list:
                self.playlist.append(song)
    
    def remove_song(self, song: Song) -> None:
        self.playlist.remove(song)

class User:
    def __init__(self, name: str, playlists: list) -> None:
        self.name = name
        self.playlists = playlists
    
    def add_playlost(self, playlist:Playlist) -> None:
        self.playlists.append(playlist)
        

class Platform:
    def search_artist(name) -> list:
        res = list()
        for artist in Artist.artists:
            if artist.name == name:
                res.append(artist)
        return res
    
    def search_album(name) -> list:
        res = list()
        for artist in Artist.artists:
            for album in artist.album_list:
                if album.name == name:
                    res.append(album)
        return res
    
    def search_song(name) -> list:
        res = list()
        for artist in Artist.artists:
            for album in artist.album_list:
                for song in album.song_list:
                    if name == song.name:
                        res.append(song)
        return res