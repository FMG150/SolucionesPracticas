Algoritmo promedio_secuencial
	Escribir "Ingresa la cantidad de notas a promediar"
	Leer n
	
	acum<- 0
	
	Para i<-1 Hasta 5 Hacer 
		Escribir "Ingrese la nota",i,":"
		Leer nota
		acum<- acum+nota
	FinPara
	prom<-acum/n
	
	Escribir "El promedio es:",prom
FinAlgoritmo
