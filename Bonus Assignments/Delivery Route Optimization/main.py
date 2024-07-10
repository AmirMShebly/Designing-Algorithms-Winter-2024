import random
import math
from typing import Dict, List, Tuple, Optional


class MultiDepotRouteOptimizer:
    def __init__(self, depots: Dict[str, Tuple[float, float]], delivery_locations: Dict[str, Tuple[float, float]],
                 assignments: Dict[str, str], iterations: int, max_route_length: Optional[float] = None,
                 time_windows: Optional[Dict[str, Tuple[float, float]]] = None,
                 capacities: Optional[Dict[str, int]] = None):

        self.depots = depots
        self.delivery_locations = delivery_locations
        self.assignments = assignments
        self.iterations = iterations
        self.max_route_length = max_route_length
        self.time_windows = time_windows
        self.capacities = capacities
        self.best_routes = self.initialize_routes()
        self.best_distance = self.calculate_total_distance(self.best_routes)

    def initialize_routes(self) -> Dict[str, List[str]]:
        routes = {depot: [] for depot in self.depots}
        for location, depot in self.assignments.items():
            routes[depot].append(location)
        for depot in routes:
            random.shuffle(routes[depot])
        return routes

    def calculate_distance(self, start: Tuple[float, float], end: Tuple[float, float]) -> float:
        return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

    def route_distance(self, depot: str, route: List[str]) -> float:
        distance = 0
        current_location = self.depots[depot]
        for location in route:
            distance += self.calculate_distance(current_location, self.delivery_locations[location])
            current_location = self.delivery_locations[location]
        distance += self.calculate_distance(current_location, self.depots[depot])
        return distance

    def calculate_total_distance(self, routes: Dict[str, List[str]]) -> float:
        total_distance = 0
        for depot, route in routes.items():
            total_distance += self.route_distance(depot, route)
        return total_distance

    def swap_mutation(self, route: List[str]) -> List[str]:
        new_route = route[:]
        i, j = random.sample(range(len(new_route)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]
        return new_route

    def inversion_mutation(self, route: List[str]) -> List[str]:
        new_route = route[:]
        i, j = sorted(random.sample(range(len(new_route)), 2))
        new_route[i:j] = reversed(new_route[i:j])
        return new_route

    def shift_mutation(self, route: List[str]) -> List[str]:
        new_route = route[:]
        i = random.randint(0, len(new_route) - 1)
        location = new_route.pop(i)
        j = random.randint(0, len(new_route))
        new_route.insert(j, location)
        return new_route

    def optimize(self):
        for iteration in range(self.iterations):
            new_routes = {}
            for depot, route in self.best_routes.items():
                mutation_type = random.choice(['swap', 'inversion', 'shift'])
                if mutation_type == 'swap':
                    new_route = self.swap_mutation(route)
                elif mutation_type == 'inversion':
                    new_route = self.inversion_mutation(route)
                else:
                    new_route = self.shift_mutation(route)
                new_routes[depot] = new_route

            new_distance = self.calculate_total_distance(new_routes)
            if new_distance < self.best_distance:
                self.best_routes = new_routes
                self.best_distance = new_distance

            if iteration % 100 == 0:
                if iteration == 0:
                    print(f'Iteration {iteration + 1}: Best distance = {self.best_distance:.2f}')
                else:
                    print(f'Iteration {iteration}: Best distance = {self.best_distance:.2f}')
            if iteration == self.iterations - 1:
                print(f'Iteration {iteration + 1}: Best distance = {self.best_distance:.2f}')

        return self.best_routes, self.best_distance


def main():
    depots = {
        'Depot1': (0, 0),
        'Depot2': (50, 50),
        'Depot3': (100, 100)
    }

    delivery_locations = {
        'Loc1': (-1, 2),
        'Loc2': (3, 4),
        'Loc3': (5, 6),
        'Loc4': (7, 8),
        'Loc5': (9, 10),
        'Loc6': (20, 25),
        'Loc7': (30, 35),
        'Loc8': (40, 45),
        'Loc9': (60, 65),
        'Loc10': (70, 75),
        'Loc11': (180, 100),
        'Loc12': (190, 195),
        'Loc13': (210, 215),
        'Loc14': (220, 325),
        'Loc15': (330, 235)
    }

    assignments = {
        'Loc1': 'Depot1',
        'Loc2': 'Depot1',
        'Loc3': 'Depot1',
        'Loc4': 'Depot1',
        'Loc5': 'Depot1',
        'Loc6': 'Depot2',
        'Loc7': 'Depot2',
        'Loc8': 'Depot2',
        'Loc9': 'Depot2',
        'Loc10': 'Depot2',
        'Loc11': 'Depot3',
        'Loc12': 'Depot3',
        'Loc13': 'Depot3',
        'Loc14': 'Depot3',
        'Loc15': 'Depot3'
    }

    optimizer = MultiDepotRouteOptimizer(depots, delivery_locations, assignments, iterations=1000)
    best_routes, best_distance = optimizer.optimize()

    print("Optimized Routes:")
    for depot, route in best_routes.items():
        print(f"{depot}: {route}")

    print(f"Total Distance: {best_distance:.2f}")


if __name__ == '__main__':
    main()

