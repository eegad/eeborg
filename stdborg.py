# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging

from eeborg import Eeborg
from config import Config

logging.basicConfig(level=logging.INFO)

borg = Eeborg(
        "stdborg",
        plugin_path="stdplugins",
        connection_retries=None,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH
)

borg.run_until_disconnected()
