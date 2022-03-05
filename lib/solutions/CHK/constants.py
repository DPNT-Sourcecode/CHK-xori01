PRODUCT_STOCK_PRICES = {
    'E': 40,
    'F': 10,
    'N': 40,
    'R': 50,
    'U': 40,
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'O': 10,
    'P': 50,
    'Q': 30,
    'S': 20,
    'T': 20,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21,
}

DISCOUNT_LIST = {
    "E": {
        "2": {
            "count": 0,
            "discount": 0,
            "discount_threshold": 2,
            "cross_product_name": "B",
        }
    },
    "A": {
        "5": {
            "count": 0,
            "discount": 50,
            "discount_threshold": 5,
        },
        "3": {
            "count": 0,
            "discount": 20,
            "discount_threshold": 3,
        },
    },
    "B": {
        "2": {
            "count": 0,
            "discount": 15,
            "discount_threshold": 2,
        }
    },
    "F": {
        "3": {
            "count": 0,
            "discount": 0,
            "discount_threshold": 3,
            "cross_product_name": "F",
        }
    },
    "H": {
        "10": {
            "count": 0,
            "discount": 20,
            "discount_threshold": 10,
        },
        "5": {
            "count": 0,
            "discount": 5,
            "discount_threshold": 5,
        },
    },
    "K": {
         "2": {
            "count": 0,
            "discount": 20,
            "discount_threshold": 2,
        },
    },
    'N': {
         "3": {
            "count": 0,
            "discount": 0,
            "discount_threshold": 3,
            "cross_product_name": "M",
        }
    },
    'P': {
         "5": {
            "count": 0,
            "discount": 50,
            "discount_threshold": 5,
        }
    },
    'Q': {
         "3": {
            "count": 0,
            "discount": 10,
            "discount_threshold": 3,
        }
    },
    'R': {
         "3": {
            "count": 0,
            "discount": 0,
            "discount_threshold": 3,
            "cross_product_name": "Q",
        }
    },
    'U': {
         "4": {
            "count": 0,
            "discount": 0,
            "discount_threshold": 4,
            "cross_product_name": "U",
        }
    },
    "V": {
        "3": {
            "count": 0,
            "discount": 20,
            "discount_threshold": 3,
        },
        "2": {
            "count": 0,
            "discount": 10,
            "discount_threshold": 2,
        },
    },
    'S': {
        '3': {
            "count": 0,
            "discount": 15,
            "discount_threshold": 3,
            "discount_group": ['S','T','X','Y','Z']
        }
    },
    'T': {
        '3': {
            "count": 0,
            "discount": 15,
            "discount_threshold": 3,
            "discount_group": ['S','T','X','Y','Z']
        }
    },
     'X': {
        '3': {
            "count": 0,
            "discount": 6,
            "discount_threshold": 3,
            "discount_group": ['S','T','X','Y','Z']
        }
    },
     'Y': {
        '3': {
            "count": 0,
            "discount": 15,
            "discount_threshold": 3,
            "discount_group": ['S','T','X','Y','Z']
        }
    },
    'Z': {
        '3': {
            "count": 0,
            "discount": 18,
            "discount_threshold": 3,
            "discount_group": ['S','T','X','Y','Z']
        }
    }
}
