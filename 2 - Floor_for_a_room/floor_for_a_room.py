from Room import Room
from Rectangle import Rectangle

print("*********Welcome*********"
      "\nThis program was made to calculate how much tiles floor would be needed to floor a room")

print("Use dot ( . ) in comma's place, for example: 139.92 ")
tile_lenght = (float(input("Type in the lenght of your [TILE] in cm: ")))
tile_width = (float(input("Type in the width of your [TILE] in cm: ")))

tile = Rectangle(tile_lenght, tile_width)

room_lenght = (float(input("Type in the lenght of your [ROOM] in meters: ")))
room_width = (float(input("Type in the width of your [ROOM] in meters: ")))

room = Room(room_lenght, room_width)

room_m2 = room.calculate_m2()
tile_cm2 = tile.calculate_cm2()

first_calculus = round(room_m2) * 10000
final_calculus = (first_calculus / tile_cm2)

print("You would need {} [TILES] for your [ROOM]".format(round(final_calculus)))