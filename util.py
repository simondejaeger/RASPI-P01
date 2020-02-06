#!/usr/bin/env python


def clean_data(data, facteur=5):
    """Fonction qui permet de lisser des tableau de donnees en enlevant les pics de bruit.

    Args:
        data: les donnees a nettoyer.
        facteur: le facteur de correction, naturel strictement superieur a 1.

    Return:
        Retourne un nouveau tableau contenant les donnees data nettoyees selon le facteur.

    """

    previous_data = []
    new_data = []
    dirty_data = []
    count = []
    is_previous_data = False
    c = 0
    for c_data in data:
        dirty_data.append(c_data)
        if len(new_data) > 0 and not is_previous_data:
            if abs(new_data[-1] - c_data) < 1:
                new_data.append(new_data[-1])
                count.append(count[-1] + 1)
            else:
                is_previous_data = True
                previous_data.append(c_data)

        elif is_previous_data:
            previous_data.append(c_data)
            if abs(new_data[-1] - c_data) < 1:
                for i in previous_data:
                    new_data.append(new_data[-1])
                    count.append(count[-1] + 1)
                previous_data = []
                is_previous_data = False

            elif len(previous_data) > facteur -1:
                is_previous_data = False
                result = []
                for i in range(facteur):
                    result.append(0)

                for i1 in range(len(previous_data)):
                    for i2 in range(i1,len(previous_data)):
                        if abs(previous_data[i1] - previous_data[i2]) < 1:
                            result[i1] += 1
                            result[i2] += 1

                m = max(result)
                new_value = new_data[-1]
                if m > 0:
                    new_value = previous_data[result.index(m)]
                else:
                    print("acacaca")

                for i in range(0, facteur):
                    new_data.append(new_value)
                    count.append(count[-1] + 1)
                previous_data = []

        elif len(new_data) == 0:
            if c_data < 1:
                new_data.append(0)
            else:
                new_data.append(c_data)
            count.append(0)

        c += 1

    return new_data
