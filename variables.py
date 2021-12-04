import os        ### para menores a python3
import pathlib   ### para mayores a python3

dir_name = os.path.dirname(os.path.abspath(__file__))

#print("Directorio actual: "+os.getcwd())
#print("Nombre base del archivo o directorio: "+os.path.basename(dir_main))
#print("Ruta existe?: "+str(os.path.exists(dir_main)))
#print("Es ruta absoluta?: "+str(os.path.isabs(dir_main)))
#print("Es un archivo?: "+str(os.path.isfile(dir_main)))
#print("Es un directorio?: "+str(os.path.isdir(dir_main)))
#print("Directorio del script: "+str(pathlib.Path(__file__).parent.absolute()))