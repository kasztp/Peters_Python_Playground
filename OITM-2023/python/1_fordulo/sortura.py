import itertools
from functools import lru_cache
import pandas as pd

# Read dataframe containing beer tour routes where each row is representing a route, with the following columns:
# - 0: starting point
# - 1: ending point
# - 2: travel time in hours between the starting and ending points
roads_df = pd.read_excel(
    '/Users/kasztp/Documents/GitHub/Python-1-inditas-elotti/2_feladat/oitm_tour.xlsx',
    header=None,
    sheet_name="TOUR_ROADS"
)

# Read dataframe containing beer tour pubs where each row is representing a pub, with the following columns:
# - 0: pub name
# - 1: number of different beers served
beers_df = pd.read_excel(
    '/Users/kasztp/Documents/GitHub/Python-1-inditas-elotti/2_feladat/oitm_tour.xlsx',
    header=None,
    sheet_name="TOUR_BEERS"
)

def route_optimizer(roads_df, beers_df):
    """
    Optimizes the route of the beer tour based on the below criteria:
    - The route is optimized if the total travel time is 24 hours and the number of beers tasted is maximized.
    - Routes can be cravelled in both directions.
    - The route starts at the FL and can end at any pub.
    - The route can contain each pub any times, but beers can be tasted only once.
    - The route can contain any number of pubs.

    :param roads_df: dataframe containing beer tour routes where each row is representing a route, with the following columns:
    - 0: starting point
    - 1: ending point
    - 2: travel time in hours between the starting and ending points
    :param beers_df: dataframe containing beer tour pubs where each row is representing a pub, with the following columns:
    - 0: pub name
    - 1: number of different beers served
    :return: number of beers tasted as int, and a list of pubs in the optimized route
    """

    # Create a dictionary of pubs with their number of beers served
    pubs = dict(zip(beers_df[0], beers_df[1]))

    # Create a dictionary of roads with their travel time
    roads = {}
    for i, row in roads_df.iterrows():
        start, end, time = row
        if start not in roads:
            roads[start] = {}
        if end not in roads:
            roads[end] = {}
        roads[start][end] = time
        roads[end][start] = time

    # Define a recursive function to find all possible routes
    @lru_cache(maxsize=None)
    def find_routes(current, visited, beers, time, routes):
        if time > 24:
            return
        if len(visited) == len(pubs) + 1:
            routes.append((beers, visited))
            return
        for pub in pubs:
            if pub not in visited:
                new_visited = tuple(list(visited) + [pub])
                new_beers = beers + pubs[pub]
                if travel_time:= get_travel_time(current, pub, roads):
                    new_time = time + travel_time
                else:
                    new_time = time
                find_routes(pub, new_visited, new_beers, new_time, routes)

    # Define a helper function to get the travel time between two pubs
    def get_travel_time(start, end, roads):
        return roads[start].get(end, 0)

    # Find all possible routes starting from FL
    routes = []
    find_routes('FL', ['FL'], 0, 0, routes)

    # Choose the route with the maximum number of beers tasted
    max_beers = 0
    max_route = None
    for beers, route in routes:
        if beers > max_beers:
            max_beers = beers
            max_route = route

    return max_beers, max_route


if __name__ == '__main__':
    print(route_optimizer(roads_df, beers_df))
