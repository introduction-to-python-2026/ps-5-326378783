def split_before_each_uppercases(formula):
    start = 0
    end = 1
    elements_lst = []
    if not formula:
        return elements_lst
    while end < len(formula):
        if formula[end].isupper():
            elements_lst.append(formula[start:end])
            start = end
        end+=1
    elements_lst.append(formula[start:])
    return elements_lst


def split_at_digit(formula):
    for char_index, char in enumerate(formula):
        if char.isdigit():
            return formula[:char_index], int(formula[char_index:])
    return formula, 1



def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    dictionary_of_atoms = {}

    for part in split_before_each_uppercases(molecular_formula):
        atom, count = split_at_digit(part)

        if atom in dictionary_of_atoms:
            dictionary_of_atoms[atom] += count
        else:
            dictionary_of_atoms[atom] = count

    return dictionary_of_atoms
        
