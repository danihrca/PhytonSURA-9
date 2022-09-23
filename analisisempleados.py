#windowsR o terminal pip install panda
import pandas as pd

tablaEmpleados= pd.read_csv("./empleados.csv")
print(tablaEmpleados.to_string())

#Filtro: Todos los datos de Analistas 1
#head es para especificar una cantidad que quiero ver
tablaAnalistas1= tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)
archivoHTML= tablaAnalistas1.to_html()
archivoTEXTO= open("datosanalistas1.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()



#Filtro: Todos los datos de Analistas 2
tablaAnalistas2= tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
archivoHTML= tablaAnalistas2.to_html()
archivoTEXTO= open("datosanalistas2.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

#Filtro: Analistas >30 años que ganen mas de 5.500millones
tablaAnalista3= tablaEmpleados[(tablaEmpleados["edad"]<30)&(tablaEmpleados["salario"]>5500000)].head(10)
archivoTEXTO= open("datosanalistas3.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()