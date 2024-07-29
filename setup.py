#                           PAQUETES DISTRIBUIDOS
#Link: https://www.youtube.com/watch?v=Zf9sN-w0BVE&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=36
from setuptools import setup

setup(
    name = "Paquetes",
    version = "1.0",
    description = "Paquete de redondeo y potencia",
    author = "Mauro Soliz",
    author_email="maurososoliz@gmail.com", #opcional
    packages = ["Paquetes","Paquetes.redondeo_potencia"] #IMPORTANTE YA QUE ESPECIFICAMOS DONDE SE ENCUENTRA EL PAQUETE
    )