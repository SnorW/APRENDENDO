frase = input('Digite uma frase')
frasef = frase.lower().strip()
frasefcount = frasef.count('a')
fraseffind = frasef.find('a')+1
fraseffindR = frasef.rfind('a')+1
print("""Sua frase possui {} A/a(s) 
O primeiro A/a aparece no espaço {}
O último A/a aparece no espaço {}""".format(frasefcount, fraseffind, fraseffindR))
