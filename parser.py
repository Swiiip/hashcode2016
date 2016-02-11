import argparse


def parse(file):
    """Parse the input file"""
    params = {}
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()
            elems = line.split(' ')
            if i == 0:  # Define the game
                params['x'], params['y'], params['nb_drones'], params['turns'], params['payload'] = [int(e) for e in elems]
            elif i == 1:  # nb _products
                params['nb_products'] = int(elems[0])
            elif i == 2:  # weights of product
                params['weights'] = [int(e) for e in elems]
            elif i == 3:
                params['nb_warehouses'] = int(elems[0])
                max_ware_i = 3 + 2*params['nb_warehouses']
                warehouses = []
            elif i <= max_ware_i:
                if i % 2 == 0:  # new warehouse
                    new_place = [int(e) for e in elems]
                else:
                    items = [int(e) for e in elems]
                    invent_dict = {}
                    for i, e in enumerate(items):
                        if e > 0:
                            invent_dict[i] = e
                    warehouses.append((new_place, invent_dict))
            elif i== max_ware_i + 1:
                params['warehouses'] = warehouses
                params['nb_orders'] = int(elems[0])
                orders = []
            elif i <= max_ware_i + 2 * params['nb_orders']:
                if i % 3 == 0:
                    new_place = [int(e) for e in elems]
                elif i % 3 == 1:
                    pass  # nb_products is not needed
                else:
                    items = [int(e) for e in elems]
                    invent = {}
                    for e in items:
                        if not e in invent:
                            invent[e] = 1
                        else:
                            invent[e] += 1
                orders.append((new_place, items))
        params['orders'] = orders
    return params


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse a file')
    parser.add_argument('file', type=str, help="File to be parsed")
    args = parser.parse_args()
    print(args)
    params = parse(args.file)
    for e in params:
        print(e)
        print(params[e])
