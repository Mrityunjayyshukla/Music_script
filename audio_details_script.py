from mutagen.easyid3 import EasyID3
import mutagen

def change_metadata(file_path, title=None, artist=None, album=None, genre=None, album_artist=None, year=None):
    try:
        audio = EasyID3(file_path)
    except mutagen.id3.ID3NoHeaderError:
        audio = mutagen.File(file_path, easy=True)
        audio.add_tags()

    if title:
        audio['title'] = title
    if artist:
        audio['artist'] = artist
    if album:
        audio['album'] = album
    if genre:
        audio['genre'] = genre
    if album_artist:
        audio['albumartist'] = album_artist
    if year:
        audio['date'] = year

    audio.save()

if __name__ == "__main__":
    file_path = "downloads/output2.mp3"
    change_metadata(file_path, title="APT.", artist="ROSE, Bruno Mars", album="APT.", genre="Chill", album_artist="ROSE", year="2024")