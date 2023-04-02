"""
Generator docstringa w stylu Pydoc/Sphinx
"""


def gen_sub_doc(list_name, params):
    """
    Funkcja zwraca string, który jest listą parametrów, atrybutów czy metod.
        Konwencja:
        <list_name>
            params[0]
            params[1]
            params[2]
            ...
    gdzie
        params[i] = [<name>, <desc>, <type>(optional)]
    """
    if params is None:
        return []
    result = "\'"+list_name+"\':\n"
    if len(params[0]) == 3:
        for param in params:
            result += f"\t{param[0]} ({param[2]}): {param[1]}\n"
    elif len(params[0]) == 2:
        for param in params:
            result += f"\t{param[0]} : {param[1]}\n"
    return result


def gen_doc_string(abstract, params):
    """
    Input:
        słownik w konwencji:
        "Etykieta": [[nazwa, opis, typ(opcjonalny)]..[..]]
    Przykładowe wejście:
        {'Args': [
                ['odmiana','trzyma odmiane owocu','str'],
                ['waga','trzyma wage gruszek','num'],
                ['smak','opisuje smak gruszek (slodki, kwasny, itd.)','str']
            ],
        'Attributes':[['odmiana','tu przechowujemy informacje o odmianie'],
        ['waga','tu przechowujemy informacje o wadze'],
        ['smak','tu przechowujemy informacje o smaku']
        ]}
    Przykładowe wyjście:

    Obiekt Gruszka opisuje nam wlasnosci gruszek.

    Args:
        odmiana (str): trzyma odmiane owocu 
        waga (num): trzyma wage gruszek
        smak (str): opisuje smak gruszek (slodki, kwasny, itd.)

    Attributes:
        odmiana: tu przechowujemy informacje o odmianie 
        waga: tu przechowujemy informacje o wadze
        smak: tu przechowujemy informacje o smaku
    """
    return "\n\n".join([abstract]+[gen_sub_doc(key, params[key]) for key in params.keys()])


"""
# Exemplary usage:

print(gen_doc_string("Obiekt Gruszka opisuje nam wlasnosci gruszek.",
        {'Args': [
                ['odmiana','trzyma odmiane owocu','str'],
                ['waga','trzyma wage gruszek','num'],
                ['smak','opisuje smak gruszek (slodki, kwasny, itd.)','str']
            ],
        'Attributes':[['odmiana','tu przechowujemy informacje o odmianie'],
        ['waga','tu przechowujemy informacje o wadze'],
        ['smak','tu przechowujemy informacje o smaku']
        ]}))
"""
