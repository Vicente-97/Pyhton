print("Hola")
year=int(input("Introduce un año: "))
month=int(input("Introduce un mes: "))
day=int(input("Introduce un día: "))
def daysofweek (year,month,day):
    a = (14-month) // 12
    y = year - a
    m = month + 12 * a - 2
    d = (day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12) % 7
    return (d)
semana=['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado']
    
print("Hoy es", (semana[daysofweek(year,month,day)]))

    
