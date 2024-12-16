from multiprocessing import Manager

# Crear colas para comunicación entre procesos
manager = Manager()

# Cola para datos de renderización
render_queue = manager.Queue()

# Cola para datos de físicas
physics_queue = manager.Queue()

# Cola para datos de comportamientos
behavior_queue = manager.Queue()

def setup_shared_data():
    """
    Función para inicializar estructuras compartidas si es necesario.
    """
    print("Colas compartidas inicializadas.")
