from molmass import Formula
import re
def get_super(x):
    normal="0123456789+-"
    super_s=" ₁₂₃₄₅₆₇₈₉⁺⁻" #ᴳᵉᵉᵏˢᶠᵒʳᴳᵉᵉᵏˢ
    return x.translate(x.maketrans(''.join(normal), ''.join(super_s)))
print('\n\n\n\t\t\t\tSimple Molar Mass and Percentage Composition Calculator\n\n[+] If there is only one of the element put a 1. For example, H2O would be entered in as H2O1\n')
while True:
    UserInput=input('[+] Enter chemical formula here: ')
    ListElementsInFormula1=[UserInput]
    SetInputToFormula=Formula(UserInput)
    UserInput=(get_super(UserInput))
    try:
        print('\n[+] The total molar mass of ' + UserInput + ' is: ' + str(SetInputToFormula.mass)+'\n')
    except:
        pass
    ElementInFormula4=iter(("".join([re.sub(r"(\d)([A-Z])", r"\1 \2", ele) for ele in ListElementsInFormula1]).split( )))
    while (1):
        val=next(ElementInFormula4, 'end')
        if val=='end':
            break
        else:
            SetElementToFormula=Formula(val)
            try:
                print(('|   '+(get_super(val))+" ="),((SetElementToFormula.mass)),('Making up'),('%.3f'%((((SetElementToFormula.mass)/(SetInputToFormula.mass)* 100)))),('% of '+UserInput))
            except:
                print('\n[+] Oops, please try again.')
    print('\n\n')
