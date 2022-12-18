from dotenv import dotenv_values

config = dotenv_values(".env")
print(config["DB_HOST"])
print(config["DB_USER"])
