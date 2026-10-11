from .custom_logger import CustomLogger

#create a single shared logger instance
_LOGGER_INSTANCE = CustomLogger()
GLOBAL_LOGGER = _LOGGER_INSTANCE.get_logger("MeridianAI_backend")