import logging

def get_logger(name="simulation"):
    """
    Configura un logger central para el proyecto.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Crear un handler para la consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Formato del log
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Añadir el handler al logger
        logger.addHandler(console_handler)

    return logger
