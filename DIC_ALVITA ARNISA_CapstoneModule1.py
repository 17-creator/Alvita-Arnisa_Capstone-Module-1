# Dictionary for Goods Stock Data
from operator import add


goods = {
    1: {'Category': 'seeds','Brand':'BISI 18', 'Spesification': 'Grow well'},
    2: {'Category': 'Herbicides', 'Brand': 'Gandewa', 'Spesification': 'Well Goods'},
    3: {'Category': 'Inseticides', 'Brand': 'Dectacron', 'Spesification': 'Well Goods'},
    4: {'Category': 'Fungicides', 'Brand': 'Bulai Cide', 'Spesification': 'Well Goods'},
    5: {'Category': 'Bactericides', 'Brand': 'Nordox', 'Spesification': 'Well Goods'},
    6: {'Category': 'Solid Fertilizer', 'Brand': 'Nitrea', 'Spesification': 'Well Goods'},
    7: {'Category': 'Liquid Fertilizer', 'Brand': 'MBS Fertilizer', 'Spesification': 'Well Goods'},
    8: {'Category': 'Others', 'Brand': 'Super Stick', 'Spesification': 'Well Goods'},
}


def main_menu():
    # Show Menu Option
    while True:
        menu_option = int(input('''
    Welcome to Agriculture Warehouse for The Farmer Good Stock
    Main Menu:
    1. Show Data Based On Categories
    2. Add Goods Stock Data
    3. Change Goods Stock Existing Data
    4. Delete Data  
    5. Menu Exity
                                
    Input Menu Option : '''))
        
        if menu_option == 1:
            # Fungsi read data
            print() 
        elif menu_option == 2:
            # fungsi create data
            add()
        elif menu_option() ==3:
            # fungsi update data
            goods.update ()
        elif menu_option == 4:
            # fungsi delete data
            del()
        elif menu_option == 5:
            # keluar dari program
            break