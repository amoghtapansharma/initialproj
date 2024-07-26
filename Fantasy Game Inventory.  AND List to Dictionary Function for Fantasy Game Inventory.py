#Fantasy Game Inventory.
def displayIncventary(group):
    item = 0
    for k,v in group.items():
        print(str(v) + ' ' + k)
        item += v
    print('Total number of items: ' + str(item))

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayIncventary(stuff)

#List to Dictionary Function for Fantasy Game Inventory.
def add_to_inventory(inventory, added_items):
    """Combine a list of loot with an inventory."""
    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = add_to_inventory(stuff, dragonLoot)
print('\n\n\n')
displayIncventary(stuff)