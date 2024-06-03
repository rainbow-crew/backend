from .base import *
import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(ROOT_DIR, '.env'))

if os.environ.get('PRODUCT_ENV') == 'prod':
    from .prod import *
else:
    from .dev import *
