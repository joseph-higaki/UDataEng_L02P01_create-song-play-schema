import yaml

class Config:
    def __init__(self):               
        with open("db_connection_config.yml", "r", encoding="utf-8") as ymlfile:  
            self._cfg = yaml.safe_load(ymlfile)

    def connection_string(self, dbname = ""):
        a = self._cfg["default-dbname"] if dbname == "" else dbname
        return f"host={self._cfg['host']} dbname={a} user={self._cfg['user']} password={self._cfg['password']}"
    