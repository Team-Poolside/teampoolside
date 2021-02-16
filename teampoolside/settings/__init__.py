import os

from .base import *

env = os.environ.get('TEAM_POOLSIDE_ENVIRONMENT')

if env == 'PROD':
    from .prod import *  # type: ignore
elif env == 'STAGE':  # TODO: do we need this?
    from .stage import *  # type: ignore
else:
    from .dev import *