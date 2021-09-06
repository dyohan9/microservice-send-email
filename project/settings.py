import environ


environ.Env.read_env(env_file=(environ.Path(__file__) - 2)(".env"))


env = environ.Env(
    # set casting, default value
    AMQP_URI=(str, "amqp://guest:guest@localhost"),
    EMAIL_HOST=(str, None),
    EMAIL_PORT=(int, 465),
    EMAIL_HOST_USER=(str, None),
    EMAIL_HOST_PASSWORD=(str, None),
    DEFAULT_FROM_EMAIL=(str, None),
)

AMQP_URI = env.str('AMQP_URI')
EMAIL_HOST = env.str('EMAIL_HOST')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL')
