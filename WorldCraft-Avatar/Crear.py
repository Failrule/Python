from os import system
import random
from numpy import row_stack
from Decodificador import Decodificar

def CrearRostro():
    rostro=[]
    def CrearPelo(rostro):
        system('clear')
        print("Estilos de pelo disponibles:\n\t1.- Denso\t\tWWWWWWWWW\n\t2.- Escaso\t\t|||||||||\n\t3.- Rapado\t\t|'''''''|\n\t4.- A raya\t\t\\\//////\nEscoja la opción: ")
        opciones=["1","2","3","4"]
        pelo=input()
        #pelo=str(random.choice(opciones))
        if pelo.isnumeric():
            pelo=int(pelo)
            if pelo == 1:
                pelo=[[1,' '],[9,'W']]
            elif pelo == 2:
                pelo=[[1,' '],[9,'|']]
            elif pelo == 3:
                pelo=[[1,' '],[1,'|'],[7,"'"],[1,'|']]
            elif pelo == 4:
                pelo=[[1,' '],[3,'\\'],[6,'/']]
            else:  
                print("Opción no valida")
        else:
            print("Debe seleccionar un número")
        rostro.append(pelo)
        return rostro
    
    def CrearOjos(rostro):
        system('clear')
        Decodificar(rostro)
        print("Estilos de ojos disponibles:\n\t1.- Normal\t\to o\n\t2.- Aburridos\t\t¬ ¬\n\t3.- Sorprendidos\t@ @\n\t4.- Enojados\t\t\ /\nEscoja la opción: ")
        opciones=["1","2","3","4"]
        Ojos=input()
        #Ojos=str(random.choice(opciones))
        if Ojos.isnumeric():
            Ojos=int(Ojos)
            if Ojos == 1:
                Ojos=[[1,' '],[1,'|'],[2,' '],[1,'o'],[1,' '],[1,'o'],[2,' '],[1,'|']]
            elif Ojos == 2:
                Ojos=[[1,' '],[1,'|'],[2,' '],[1,'¬'],[1,' '],[1,'¬'],[2,' '],[1,'|']]
            elif Ojos == 3:
                Ojos=[[1,' '],[1,'|'],[2,' '],[1,'@'],[1,' '],[1,'@'],[2,' '],[1,'|']]
            elif Ojos == 4:
                Ojos=[[1,' '],[1,'|'],[2,' '],[1,'\\'],[1,' '],[1,'/'],[2,' '],[1,'|']]
                print("4")
            else:  
                print("Opción no valida")
        else:
            print("Debe seleccionar un número")
        rostro.append(Ojos)
        return rostro

    def CrearOrejasNariz(rostro):
        system('clear')
        Decodificar(rostro)
        print("Estilos de oreas y nariz disponibles:\n\t1.- Normal\t\t(  L  )\n\t2.- Vampiro\t\t<  V  >\n\t3.- Pequeños\t\td  u  b\nEscoja la opción: ")
        opciones=["1","2","3"]
        OrejasNariz=input()
        #OrejasNariz=str(random.choice(opciones))
        if OrejasNariz.isnumeric():
            OrejasNariz=int(OrejasNariz)
            if OrejasNariz == 1:
                OrejasNariz=[[1,'('],[4,' '],[1,'L'],[4,' '],[1,')']]
            elif OrejasNariz == 2:
                OrejasNariz=[[1,'<'],[4,' '],[1,'V'],[4,' '],[1,'>']]
            elif OrejasNariz == 3:
                OrejasNariz=[[1,'d'],[4,' '],[1,'u'],[4,' '],[1,'b']]
            else:  
                print("Opción no valida")
        else:
            print("Debe seleccionar un número")
        rostro.append(OrejasNariz)
        return rostro
            
    def CrearBoca(rostro):
        system('clear')
        Decodificar(rostro)
        print("Estilos de boca disponibles:\n\t1.- Normal\t\t--\n\t2.- Vampiro\t\tv-v\n\t3.- Pequeña\t\t-\nEscoja la opción: ")
        opciones=["1","2","3"]
        Boca=input()
        #Boca=str(random.choice(opciones))
        if Boca.isnumeric():
            Boca=int(Boca)
            if Boca == 1:
                Boca=[[1,' '],[1,'|'],[2,' '],[1,'---'],[2,' '],[1,'|'],[1,' ']]
            elif Boca == 2:
                Boca=[[1,' '],[1,'|'],[2,' '],[1,'v-v'],[2,' '],[1,'|'],[1,' ']]
            elif Boca == 3:
                Boca=[[1,' '],[1,'|'],[3,' '],[1,'-'],[3,' '],[1,'|'],[1,' ']]
            else:  
                print("Opción no valida")
        else:
            print("Debe seleccionar un número")
        rostro.append(Boca)
        return rostro

    def CrearCuello(rostro):
        system('clear')
        Decodificar(rostro)
        print("Estilos de cuello disponibles:\n\t1.- Normal\t\t|   |\n\t2.- Vampiro\t\t|\ /|\n\t3.- Grueso\t\t|  |\nEscoja la opción: ")
        opciones=["1","2","3"]
        Cuello=input()
        #Cuello=str(random.choice(opciones))
        if Cuello.isnumeric():
            Cuello=int(Cuello)
            if Cuello == 1:
                Cuello=[[2,' '],[1,'\\'],[5,'_'],[1,'/'],[2,' ']]
            elif Cuello == 2:
                Cuello=[[2,' '],[1,'\\'],[5,'v'],[1,'/'],[2,' ']]
            elif Cuello == 3:
                Cuello=[[1,' '],[1,'|'],[7,'_'],[1,'|'],[3,' ']]
            else:  
                print("Opción no valida")
        else:
            print("Debe seleccionar un número")
        rostro.append(Cuello)
        return rostro
    
    def CrearNombre(rostro):
        system("clear")
        Decodificar(rostro)
        print("Escriba un nombre para el rostro")
        nombre=input()
        archivo=open(nombre, mode="w")
        for i in rostro:
            for j in i:
                for k in j:
                    archivo.write(str(k))
            archivo.write(str("\n"))
        archivo.close()

    rostro=CrearPelo(rostro)
    rostro=CrearOjos(rostro)
    rostro=CrearOrejasNariz(rostro)
    rostro=CrearBoca(rostro)
    rostro=CrearCuello(rostro)
    CrearNombre(rostro)
