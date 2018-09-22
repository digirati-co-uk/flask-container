import os

EXAMPLE_VARIABLE = os.getenv(key="EXAMPLE_VARIABLE", default="default value")
DEBUG = bool(os.getenv(key="DEBUG", default="False"))
