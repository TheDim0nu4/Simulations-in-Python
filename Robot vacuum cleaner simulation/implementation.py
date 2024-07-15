import random
import matplotlib.pyplot as plt


class Room:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.room = list()
        for w in range(self.width):
            self.room.append(list())
            for _ in range(self.length):
                self.room[-1].append(0)


    def add_dust(self, count):
        for _ in range(count):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.length-1)
            self.room[x][y] += 1


    def has_position(self, pos):
        return pos[0] >= 0 and pos[0] < self.width and pos[1] >= 0 and pos[1] < self.length


    def has_dust(self, pos):
        if self.has_position(pos) is False:
            raise ValueError("Bad position")
        
        return self.room[pos[0]][pos[1]] > 0


    def pickup_dust(self, pos):
        if self.has_dust(pos) is True:
            self.room[pos[0]][pos[1]] -= 1


    def is_clean(self):
        for w in self.room:
            for l in w:
                if l != 0: return False
        return True


    def get_width(self):
        return self.width
    

    def get_length(self):
        return self.length


class VacuumCleaner:
    def __init__(self, start_pos, room):
        self.current_position = start_pos
        self.possible_directions = ['N', 'E', 'S', 'W']
        self.room = room

    def move(self, direction):
        if self.room.has_dust(self.current_position):
            self.room.pickup_dust(self.current_position)
            return
        
        if direction not in self.possible_directions:
            raise ValueError("This direction not in possible_directions")
        
        new_position = list(self.current_position)
        
        if direction == 'N' and new_position[0] - 1 >= 0:
            new_position[0] -= 1
        elif direction == 'S' and new_position[0] + 1 < self.room.get_width():
            new_position[0] += 1
        elif direction == 'E' and new_position[1] - 1 >= 0:
            new_position[1] -= 1
        elif direction == 'W' and new_position[1] + 1 < self.room.get_length():
            new_position[1] += 1

        if self.room.has_position(new_position):
            self.current_position = tuple(new_position)

    
def simulate_cleaning(room_dimensions, dust_count, simulation_no):
    all_steps = list()
    for _ in range(simulation_no):
        room = Room( room_dimensions[0], room_dimensions[1] )
        room.add_dust(dust_count)

        x = random.randint(0, room.get_width()-1)
        y = random.randint(0, room.get_length()-1)
        cleaner = VacuumCleaner( (x, y), room )

        possible_directions = ['N', 'E', 'S', 'W']
        num_steps = 0
        while room.is_clean() is False:
            cleaner.move(random.choice(possible_directions))
            num_steps += 1

        all_steps.append(num_steps)

    return all_steps


def main():
    steps = simulate_cleaning((5, 3), 50, 15)

    plt.hist(steps, bins=5, edgecolor='black')

    plt.title('Distribution of the necessary steps to clean the room')
    plt.xlabel('Values')
    plt.ylabel('Frekvencia')

    plt.show()


if __name__ == '__main__':
    main()
