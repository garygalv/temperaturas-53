# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Milagro
        [   # Semana 1
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 33}
        ]
    ],
    [   # Naranjito
        [   # Semana 1
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 35},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 37},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 39},
            {"day": "Domingo", "temp": 23}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 29}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Milagro", "Naraanjito", "Guayaquil"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")