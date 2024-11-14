import uuid
from interfazAWS import InterfazAWS
import logging

logging.basicConfig(level=logging.ERROR)

def main():
    config_data = {
        "session_id": str(uuid.uuid4()),
        "cpu_id": str(uuid.getnode()),
        "id": "UADER-FCyT-IS2",
    }

    singleton = InterfazAWS(config_data["session_id"], config_data["cpu_id"])

    print("\nConsulta de datos en CorporateData:")
    print(singleton.consultar_datos_sede(config_data["session_id"], config_data["cpu_id"], config_data["id"]))

    print("\nConsulta el CUIT en CorporateData:")
    print(singleton.consultar_cuit(config_data["session_id"], config_data["cpu_id"], config_data["id"]))

    print("\nGenera un nuevo ID de secuencia en CorporateData:")
    print(singleton.generar_id_secuencia(config_data["session_id"], config_data["cpu_id"], config_data["id"]))

    print("\nRegistra acción en CorporateLog:")
    print(singleton.registrar_log())

    print("\nRegistros asociados al CPU actual:")
    print(singleton.listar_logs(filtro="cpu"))

    print("\nSesion actual:")
    print(singleton.listar_logs(filtro="session"))

if __name__ == "__main__":
    main()
