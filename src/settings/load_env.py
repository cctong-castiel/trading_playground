import os
from dotenv import load_dotenv

load_dotenv(override=True)

class ConfigBase:
    """
    A base configuration class that loads environment variables.

    Attributes:
        _config (dict): A dictionary to store configuration key-value pairs.
    """

    def __init__(self):
        """
        Initialize the CoinfigBase instance and setups the _config dictionary.
        """
        self._config = {}
        
    def _get_and_check_variable(self, key, cast, default_value):
        """
        Retrieves, checks, and casts environment variables.

        Args:
            key (str): The environment variable key.
            cast (type): The type to cast the variable to.
            default_value: The default value if the environment variable is not set.
        
        Returns:
            The value of the environment variable after casting it ito the specified type.

        Raises:
            ValueError: If the environment variable cannot be cast to the specified type.
        """
        value = os.getenv(key)
        if value is None:
            if default_value is None:
                raise ValueError(f"Environment variable '{key}' is not set and no default value provided.")
            else:
                value = default_value
        
        try:
            if cast is bool:
                return eval(value)
            return cast(value)
        except ValueError:
            raise ValueError(f"Environment variable '{key}' cannot be cast to {cast.__name__}.")
        
    def __setattr__(self, name, value):
        """
        Sets an attribute and stores it in the _config dictionary.

        Args:
            name (str): The name of the attribute.
            value (tuple): The value of the attribute.

        Raises:
            ValueError: If the environment variable cannot be cast to the specified type.
        """
        if name != "_config":
            if isinstance(value, tuple):
                self._config[name] = value
                if len(value) == 2:
                    default_value = None
                else:
                    default_value = value[2]
                value = self._get_and_check_variable(value[0], value[1], default_value)
            else:
                self._config[name] = value
        super().__setattr__(name, value)

class Environment(ConfigBase):
    """
    A configuration class that loads specific environment variables.

    Attributes:
        LOG_LEVEL (str): The Log level of the logger.
        TURN_ON_LOGGING (str): A switch for turning logging or not.
    """

    def __init__(self):
        """
        Initialize the Environment instance and sets up specific environment variables.
        """
        super().__init__()
        self.LOG_LEVEL = ("LOG_LEVEL", str)
        self.TURN_ON_LOGGING = ("TURN_ON_LOGGING", str)