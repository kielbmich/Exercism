def get_list_of_wagons(*wagons):
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    one, two, three, *remaining = each_wagons_id
    return [three, *missing_wagons, *remaining, one, two]


def add_missing_stops(route, **stops):
    route.update({"stops" : [*stops.values()]})
    return route


def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    return list(map(list, zip(*wagons_rows)))