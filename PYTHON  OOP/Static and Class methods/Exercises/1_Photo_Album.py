from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        for i in range(pages):
            self.photos.append([])


    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for p in range(self.pages):
            if len(self.photos[p]) < 4:
                self.photos[p].append(label)
                return f"{label} photo added successfully on page " \
                       f"{p + 1} slot " \
                       f"{len(self.photos[p])}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        current_page = []
        for page in self.photos:
            for picture in page:
                if picture == 0:
                    current_page.append("  ")
                else:
                    current_page.append("[]")
            result += f"{' '.join(current_page)}\n"
            current_page = []
            result += "-----------\n"
        result = result[:-1:]
        return result


# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))

# print(album.display())





