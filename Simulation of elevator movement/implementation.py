import random

import matplotlib.pyplot as plt


class Worker:
    def __init__(self, start_floor, goal_floor):
        self.start_floor = start_floor
        self.goal_floor = goal_floor

    def get_goal_floor(self):
        return self.goal_floor

class Elevator:
    def __init__(self, capacity, current_floor=0):
        self.capacity = capacity
        self.current_floor = current_floor
        self.moving_up = True

        self.passengers = []


    def move(self):
        if self.moving_up is True:
            self.current_floor += 1
        else:
            self.current_floor -= 1


    def get_passenger_count(self):       
        return len(self.passengers)


    def change_direction(self):
        self.moving_up = not self.moving_up


    def add_passenger(self, passenger):
        if self.capacity == len(self.passengers):
            return False
        
        self.passengers.append(passenger)
        return True


    def remove_passenger(self, passenger):
        if passenger not in self.passengers:
            return
    
        self.passengers.remove(passenger)
        if self.moving_up is True and len(self.passengers) == 0:
            self.change_direction()

    def get_current_floor(self):
        return self.current_floor
    
    def get_passengers(self):
        return self.passengers
    
    def get_moving_up(self):
        return self.moving_up
            

class Building:
    def __init__(self, floor_count, elevator_count, elevator_capacity):
        self.floor_count = floor_count
        self.elevators = []
        for _ in range(elevator_count):
            self.elevators.append(
                Elevator(elevator_capacity))

        self.floors = []
        for _ in range(floor_count):
            self.floors.append([])


    def add_worker_to_floor(self, worker, floor):
        self.floors[floor].append(worker)


    def is_waiting(self):
        return len(self.floors[0])


    def time_step(self):
        for elevator in self.elevators:
            num_top = elevator.get_current_floor()
            
            for worker in elevator.get_passengers():
                if worker.get_goal_floor() == num_top:
                    elevator.remove_passenger(worker)

            if elevator.get_moving_up() is True:
                for worker_wait in self.floors[num_top]:
                    if elevator.add_passenger(worker_wait) is True:
                        self.floors[num_top].remove(worker_wait)

            elevator.move()
            if elevator.get_current_floor() == 0 or elevator.get_current_floor() == self.floor_count-1:
                elevator.change_direction()


    def get_floor_count(self):
        return self.floor_count
    

def simulate_workday(number_of_workers, floor_count, number_of_elevators, elevator_capacity):
    waiting_counts = []
    
    build = Building( floor_count, number_of_elevators, elevator_capacity )
    
    workers_in_simulate = 0
    for _ in range( random.randint(1, 5) ):
        worker = Worker( 0, random.randint(1, build.get_floor_count()-1) )
        build.add_worker_to_floor(worker, 0)
        workers_in_simulate += 1

    while number_of_workers != workers_in_simulate or build.is_waiting() != 0:
        build.time_step()
        waiting_counts.append(build.is_waiting())

        if workers_in_simulate < number_of_workers:
            for _ in range( random.randint(1, 5) ):
                worker = Worker( 0, random.randint(1, build.get_floor_count()-1) )
                build.add_worker_to_floor(worker, 0)
                workers_in_simulate += 1
                if workers_in_simulate == number_of_workers:
                    break    

    return waiting_counts


def main():
    steps = simulate_workday(1000, 10, 10, 4)

    x = [i for i in range(0, len(steps))]
    y = steps

    plt.plot(x, y)
    plt.xlabel('Simulation steps')
    plt.ylabel('Number of people waiting')
    plt.title('Simulation of elevators')
    plt.show()


if __name__ == '__main__':
    main()
