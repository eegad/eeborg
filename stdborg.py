# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import logging

from config import Config
from eeborg import Eeborg

argument = argparse.ArgumentParser()
argument.add_argument('-s', '--session',
                      default='eeborg',
                      help='Set session name')

arg = argument.parse_args()

session_name = arg.session

logging.basicConfig(level=logging.INFO)

borg = Eeborg(
    session_name,
    plugin_path="stdplugins",
    connection_retries=None,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

borg.run_until_disconnected()
