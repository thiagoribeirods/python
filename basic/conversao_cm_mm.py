print("Convertendo metros em cm e mm")

metros = float(input("Valor em metros: "))

cm = metros * 100
mm = cm * 10

print("{:.0f} equivale a {:0f}cm e equivale a {:.0f}mm".format(metros,cm,mm))
