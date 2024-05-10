from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.__guests = 0

    def _find_room_by_number(self, number):
        room = None
        for r in self.rooms:
            if r.number == number:
                room = r
                break
        return room

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    @property
    def guests(self):
        return self.__guests

    @guests.setter
    def guests(self, value):
        guests = sum([r.guests for r in self.rooms])
        self.__guests = guests

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = self._find_room_by_number(room_number)
        if room and not room.is_taken and people <= room.capacity:
            room.is_taken = True
            room.guests = people
            self.guests += people

    def free_room(self, room_number):
        room = self._find_room_by_number(room_number)
        if room and room.is_taken:
            room.is_taken = False
            room.guests = 0
            self.guests -= room.guests

    def status(self):

        free_rooms_numbers = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms_numbers = [str(room.number) for room in self.rooms if room.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests" \
               f"\nFree rooms: {', '.join(free_rooms_numbers)}" \
               f"\nTaken rooms: {', '.join(taken_rooms_numbers)}"
