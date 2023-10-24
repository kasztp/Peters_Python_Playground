import pandas as pd

# load stations.xlsx
stations = pd.read_excel('OITM-2023/python/2_feladat/stations.xlsx', header=None)
# rename 1st column to price
stations.rename(columns={0: 'price'}, inplace=True)


def station_optimizer(stations: pd.DataFrame) -> int:
    """Florian's gas cost optimizer.
    
    Florian's car is out of gas, fortunately he starts at the first station in the dataframe.
    His car can hold 40 litres of gas, and he wants to get to the last station in the dataframe from the cheapest cost.
    Distance between each stations is 100 km, and the car uses 10 litres of gas per 100 km.
    He can only buy gas at the stations, and he can only buy that many which fits his gas tank.
    Each station has unlimited amount of gas.
    Return the minimum amount which is enough to cover the whole trip.
    Optimize to get the maximum possible amount on the cheapest stations to minimize total gas cost.

    :param stations: pandas.DataFrame - the stations with their gas prices in one column called price
    :return: int - the minimum amount which is enough to cover the whole trip
    """
    stations = stations.sort_values(by='price')
    total_cost = 0
    remaining_distance = len(stations) * 100
    tank = 0  # Initial full tank

    for _, station in stations.iterrows():
        if tank * 10 >= remaining_distance:
            # Enough gas to reach the end
            break
        else:
            # Buy gas at this station
            gas_needed = 40 - tank  # Fill up the tank
            total_cost += gas_needed * station['price']
            tank = 40  # Reset the tank
        remaining_distance -= 100  # Move to the next station

    return total_cost


if __name__ == "__main__":
    print(station_optimizer(stations))
