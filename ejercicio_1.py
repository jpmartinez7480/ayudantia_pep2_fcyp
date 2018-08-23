import numpy as np

#sueldo_liquido = ti - (pp*ti) - ps*ti + bni

sueldoBase = input("Ingrese lista de sueldo base: ")
asignacionImponible = input("Ingrese lista de asignacion imponible: ")
porcentajePrevison = input("Ingrese lista porcentaje de prevision: ")
porcentajeSalud = input("Ingrese lista porcentaje de salud: ")
bonosNoImponibles = input("Ingrese lista bonos no imponibles: ")

#Procesamiento
sueldoBase = np.array(sueldoBase)
asignacionImponible = np.array(asignacionImponible)
porcentajePrevison = np.array(porcentajePrevison)
porcentajeSalud = np.array(porcentajeSalud)
bonosNoImponibles = np.array(bonosNoImponibles)

totalImponible = sueldoBase + asignacionImponible
listado_porcentaje_prevision = porcentajePrevison/100.0
listado_porcentaje_salud = porcentajeSalud/100.0

porcentajePrevison_descuento = listado_porcentaje_prevision*totalImponible
porcentajeSalud_descuento = listado_porcentaje_salud*totalImponible

sueldosLiquido = totalImponible - porcentajePrevison_descuento - porcentajeSalud_descuento + bonosNoImponibles


print sueldosLiquido

