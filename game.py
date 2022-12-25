import makechar
import monsters
import other_mechanics
import roomgen
import start 
import townloop



start.menu()
character = start.jatka_pelia()
while True:
    townloop.actions(character)
    dungeon = roomgen.Ungeon()
    while True:
        dungeon.choose_action()
        if len(dungeon.rooms) > 6:
            character.gold += 100
            print("You completed the dungeon! Returning to town")
            break