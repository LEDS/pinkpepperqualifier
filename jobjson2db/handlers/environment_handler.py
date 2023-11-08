from dotenv import load_dotenv
import json
import os

class EnvironmentException(Exception):
    pass


class EnvironmentHandler:
    # Environment Variables
    envVar_exception = "EXCEPTION_ENVIRONMENTHANDLER"
    # Exceptions Keys
    exception_getJsonNoEnvVar = "NONEXISTENT_JSON_FILE"
    exception_getJsonSyntax = "SYNTAX_JSON_FILE"

    def get_json(self, *, envVar: str, raise_exception: bool = True) -> dict:
        filename = self.env.get(envVar)
        if raise_exception and filename is None:
            raise EnvironmentException(self.exception_msg.get(self.exception_getJsonNoEnvVar, ""))

        data = {}
        try:
            with open(filename, "r") as f:
               data = json.load(f)
        except:
            if raise_exception:
                raise EnvironmentException(self.exception_msg.get(self.exception_getJsonSyntax, ""))
        return data


    def __init__(self):
        load_dotenv()
        self.env = os.environ

        self.exception_msg = {}
        self.exception_msg = self.get_json(
            envVar = self.envVar_exception,
            raise_exception = False)