class usables:

    USABLES = {
        # Usable
        'Pen':                {'klass': 'Pen',          'weight':  20},
        'MobilePhone':        {'klass': 'MobilePhone',  'weight': 488},
        'Lighter':            {'klass': 'Lighter',      'weight':  22},
        'Torch':              {'klass': 'Lighter',      'weight': 377},
        'Fireplace':          {'klass': 'Fireplace',    'weight': 800},
        'Bottle':             {'klass': 'Bottle',       'weight':  42},
        'Twig':               {'klass': 'Recipe',       'weight':  60},
        'Branch':             {'klass': 'Recipe',       'weight': 333},
        'Rags':               {'klass': 'Recipe',       'weight': 333},
        'Petrol':             {'klass': 'Recipe',       'weight': 512},
        'Tissu':              {'klass': 'Recipe',       'weight': 40},
        'WieldStick':         {'klass': 'Recipe',       'weight': 85},
        'Gunpowder':          {'klass': 'Recipe',       'weight': 1},
        'Coal':               {'klass': 'Recipe',       'weight': 10},
        'Sulfur':             {'klass': 'Recipe',       'weight': 10},
        'Saltpeter':          {'klass': 'Recipe',       'weight': 10},
        'Fuse':               {'klass': 'Recipe',       'weight': 6},
        'WalkieTalkie':       {'klass': 'WalkieTalkie', 'weight': 820},
        'OldSpeaker':         {'klass': 'WalkieTalkie', 'weight': 520},
        'Wires':              {'klass': 'WalkieTalkie', 'weight': 120},
        'Battery':            {'klass': 'WalkieTalkie', 'weight': 180},

        # Heal
        'Painkiller':         {'klass': 'Usable',      'level':  0, 'weight': 50,  'ef': {'p_hp': 1}},
        'Medkit':             {'klass': 'Usable',      'level':  2, 'weight': 500, 'ef': {'p_hp': 10}},
        'Stimulant':          {'klass': 'Usable',      'level':  3, 'weight': 200, 'ef': {'p_hp': 15}},

        # Consumeable
        'Coke':               {'klass': 'Consumable',  'level':  1, 'weight': 333,  'price': 8,  'ef': {'thirst': 150}},
        'Pizza':              {'klass': 'Consumable',  'level':  1, 'weight': 517,  'price': 25,  'ef': {'thirst': 150}},
        'EnergyDrink':        {'klass': 'Consumable',  'level':  1, 'weight': 200,  'price': 25,  'ef': {'thirst': 100}},
        'Sandwich':           {'klass': 'Consumable',  'level':  1, 'weight': 436,  'price': 12,  'ef': {'thirst': -30, 'hunger': 250}},
        'SmallBeer':          {'klass': 'Consumable',  'level':  2, 'weight': 350,  'price': 12,  'ef': {'thirst': 150, 'hunger':  50, 'alcohol': 2}},
        'LargeBeer':          {'klass': 'Consumable',  'level':  1, 'weight': 530,  'price': 12,  'ef': {'thirst': 250, 'hunger': 100, 'alcohol': 3}},
        'Water1.5':           {'klass': 'Consumable',  'level':  1, 'weight': 1510, 'price': 24, 'ef': {'thirst': 550}},
        'Water0.5':           {'klass': 'Consumable',  'level':  1, 'weight': 510,  'price': 12, 'ef': {'thirst': 170}},
        'Hash':                {'klass': 'QuestItem',   'level':  2, 'weight': 1,    'price': 30, 'ef': {'thirst': -1000}},
        'Apple':              {'klass': 'Consumable', 'level': 1, 'weight': 160, 'price': 2, 'ef': {'hunger': 150, 'thirst': 150}},
        'InstantNoodles':     {'klass': 'Consumable', 'level': 1, 'weight': 90, 'price': 4, 'ef': {'hunger': 200, 'thirst': 50}},
        'WaterBottle':        {'klass': 'FilledBottle', 'level': 1, 'weight': 560, 'price': 8, 'ef': {'hunger': 0, 'thirst': 500}},
        'Cocaine':            {'klass': 'Drugs', 'level': 34, 'weight': 1, 'price': 100, 'ef': {'high': 1}},
        'Speed':              {'klass': 'Drugs', 'level': 20, 'weight': 1, 'price':  20, 'ef': {'high': 1}},
        'Extasy':             {'klass': 'Drugs', 'level': 18, 'weight': 2, 'price':  30, 'ef': {'high': 1}},
        'Weed':               {'klass': 'Drugs', 'level': 18, 'weight': 1, 'price':  20, 'ef': {'high': 1}},

        # Quest Items
        'ArmyLetter':         {'klass': 'Email',       'key': 'sdqa_email_army'},
        'NoteGizmore':        {'klass': 'Note',        'key': 'sd_note_gizmore'},
        'TheosPurse':         {'klass': 'TheosPurse',  'key': 'sd_theo_purse'},
        'Intolerance':        {'klass': 'Intolerance',},

    }
