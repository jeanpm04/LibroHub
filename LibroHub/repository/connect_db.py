from sqlmodel import create_engine

#conexión a la base de datos
def connect():
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/librohub_db")
    return engine