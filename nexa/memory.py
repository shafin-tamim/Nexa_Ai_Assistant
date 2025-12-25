from config.logger import get_logger

logger = get_logger(__name__)

class Memory:
    def __init__(self):
        self.history = []
        logger.info("Memory initialized")

    def add(self, role, message):
        self.history.append({"role": role, "content": message})
        logger.info(f"Memory added: {role}")

    def clear(self):
        self.history = []
        logger.info("Memory cleared")
