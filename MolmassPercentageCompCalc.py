from molmass import Formula
import re

def get_super(x):
    normal = "0123456789+-"
    super_s = " ₁₂₃₄₅₆₇₈₉⁺⁻"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

print('\n\n\n\t\t\t\tSimple Molar Mass and Percentage Composition Calculator\n\n')
print('[+] If there is only one of the element put a 1. For example, H2O would be entered in as H2O1\n')

while True:
    UserInput=input('[+] Enter chemical formula here: ')

    # Add user input to list so it can be seperated into a list, user input is made into list here so were able to format it
    ListElementsInFormula1=[UserInput]
    # Adds spaces inbetween elements so it can be formatted next
    ListElementsInFormula2=[re.sub(r"(\d)([A-Z])", r"\1 \2", ele) for ele in ListElementsInFormula1]
    # Putl list of elemnts back into string
    ListElementsInFormula3="".join(ListElementsInFormula2)
    # Once list of elements is seperated by spaces and in string, this uses each space to seperate each element into its own item back in a list
    ListElementsInFormula4=(ListElementsInFormula3.split( ))

    SetInputToFormula=Formula(UserInput)

    # display superscipt

    UserInput = (get_super(UserInput)) #ᴳᵉᵉᵏˢᶠᵒʳᴳᵉᵉᵏˢ
    print('\n[+] The total molar mass of ' + UserInput + ' is: ' + str(SetInputToFormula.mass)+'\n')

    # converting list to iterator
    ElementInFormula4 = iter(ListElementsInFormula4)
    while (1):
        val = next(ElementInFormula4, 'end')
        # Goes down list of seperated elemnts and prints there molar mass
        if val == 'end':
            break
        else:
            SetElementToFormula = Formula(val)
            ElementMass=(SetElementToFormula.mass)
            print(('|   '+(get_super(val))+" ="),(ElementMass))
    print('\n\n')
