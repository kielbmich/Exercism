def create_inventory(items):
    inventory = {}
    return add_items(inventory, items)

def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def decrement_items(inventory, items):
    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
    return inventory

def remove_item(inventory, item):
    if item in inventory.keys():
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    return [(key, inventory[key]) for key in inventory if inventory[key] > 0]