# SEX
# 0 - WOMAN
# 1 - MAN

# PHYSICAL ACTIVITY
# 0 - Sedentary
# 1 - Light activity
# 2 - Moderate activity
# 3 - Intense activity
# 4 - Very intense activity

"""
Los hombres necesitan 1 caloría por kilogramo de peso y hora:
Peso en Kg x 1 caloría x 24 horas
Las mujeres necesitan 0,9 calorías por kilogramo de peso y hora:
Peso en Kg x 0,9 calorías x 24 horas

Sedentario (sin ejercicio): 1,2 x MB.
Actividad ligera (caminar, deportes con poco gasto energético): 1,375 x MB.
Actividad moderada (actividades como correr, bailar… 3-4 días por semana): 1,55 x MB.
Actividad intensa (natación, ciclismo… 5-6 días por semana): 1,725 x MB.
Actividad muy intensa (ejercicio intenso todos los días de la semana): 1,9 x MB.
"""


def calories(sex, weight, physical_activity):

    total_calories = 0

    # SEX
    if sex == 1:
        total_calories = weight * 24

    elif sex == 0:
        total_calories = weight * 0.9 * 24

    else:
        exit()

    # PHYSICAL ACTIVITY
    if physical_activity == 0:
        total_calories = total_calories * 1.2

    elif physical_activity == 1:
        total_calories = total_calories * 1.375

    elif physical_activity == 2:
        total_calories = total_calories * 1.55

    elif physical_activity == 3:
        total_calories = total_calories * 1.725

    elif physical_activity == 4:
        total_calories = total_calories * 1.9

    else:
        exit()

    return f"Calories needed: {int(total_calories)}"
