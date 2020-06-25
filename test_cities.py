from cities import *
import pytest
import random


def test_compute_total_distance():

    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert compute_total_distance(road_map1) == pytest.approx(9.386 + 18.496 + 10.646, 0.01)

    road_map2 = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                 ('Wyoming', 'Cheyenne', 41.145548, -104.802042),
                 ('Washington', 'Olympia', 47.042418, -122.893077)]

    assert compute_total_distance(road_map2) == pytest.approx(20.5 + 39.448 + 19.028, 0.01)

    # testing edge cases
    road_map3 = [('A', 'a', 0.0, 0.0),
                 ('B', 'b', 90.0, -180.0),
                 ('C', 'c', -90.0, 180.0)]

    assert compute_total_distance(road_map3) == pytest.approx(201.246 + 402.492 + 201.246, 0.01)

    # testing max distances with random variables
    road_map4 = [('A', 'a', random.uniform(-90.0, 90.0), random.uniform(-180.0, 180.0)),
                 ('B', 'b', random.uniform(-90.0, 90.0), random.uniform(-180.0, 180.0)),
                 ('C', 'c', random.uniform(-90.0, 90.0), random.uniform(-180.0, 180.0))]

    assert compute_total_distance(road_map4) <= 18 + 360 + 402.492

    # testing type of the output
    assert type(compute_total_distance(road_map3)) == float


def test_swap_cities():

    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094),
                 ("Wyoming", "Cheyenne", 41.145548, -104.802042)]

    # checking the output
    assert len(swap_cities(road_map1, 1, 2)) == 2
    assert type(swap_cities(road_map1, 1, 2)) == tuple

    new_road_map1, new_total_distance1 = swap_cities(road_map1, 1, 2)

    # testing when cities are replaced with different index numbers
    assert new_road_map1 != road_map1
    assert new_total_distance1 != compute_total_distance(road_map1)

    # testing with the edge coordinates
    road_map2 = [('A', 'a', 0.0, 0.0),
                 ('B', 'b', 90.0, -180.0),
                 ('C', 'c', -90.0, 180.0)]

    new_road_map2, new_total_distance2 = swap_cities(road_map1, 0, 1)

    # testing when cities are replaced with different index numbers
    assert new_road_map2 != road_map2
    assert new_total_distance2 != compute_total_distance(road_map2)

    # testing when the same indexes are entered
    new_road_map3, new_total_distance3 = swap_cities(road_map2, 1, 1)
    assert new_road_map3 == road_map2
    assert new_total_distance3 == compute_total_distance(road_map2)


def test_shift_cities():

    road_map1 = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                 ('Wyoming', 'Cheyenne', 41.145548, -104.802042),
                 ('Washington', 'Olympia', 47.042418, -122.893077),
                 ('Kentucky', 'Frankfort', 38.197274, -84.86311)]

    # there should be some changes between the output and the input
    assert shift_cities(road_map1) != road_map1
    assert len(shift_cities(road_map1)) == len(road_map1)

    # checking the output type
    assert type(shift_cities(road_map1)) == list

    # test for the last items
    assert shift_cities(road_map1)[0] == road_map1[3]

    # test for remaining parts
    assert shift_cities(road_map1)[1] == road_map1[0]
    assert shift_cities(road_map1)[2] == road_map1[1]
    assert shift_cities(road_map1)[3] == road_map1[2]
