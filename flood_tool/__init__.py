from geo import *
from tool import *
from live import *

import pandas as pd


if __name__ == '__main__':
    t = Tool("postcodes.csv", "flood_probability.csv", "property_value.csv")
    t.get_lat_long(["CT147DB", "TN103PU"])
    print(t.get_easting_northing_flood_probability_band([526645], [179284]))