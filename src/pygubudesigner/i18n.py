#
# Copyright 2012-2022 Alejandro Autalán
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import gettext
import locale
import os
import sys
from pathlib import Path

import pygubu.i18n as pygubu_i18n

# Change this variable to your app name!
#  The translation files will be under
#  @LOCALE_DIR@/@LANGUAGE@/LC_MESSAGES/@APP_NAME@.mo
#
APP_NAME = "pygubu-designer"

# Not sure in a regular desktop:

DATA_DIR = Path(__file__).parent / "data"
LOCALE_DIR = DATA_DIR / "locale"

# Now we need to choose the language. We will provide a list, and gettext
# will use the first translation available in the list
#
#  In maemo it is in the LANG environment variable
#  (on desktop is usually LANGUAGES)
#
DEFAULT_LANGUAGES = os.environ.get("LANG", "").split(":")

# Try to get the languages from the default locale
languages = []
lc, encoding = locale.getlocale()
if lc:
    languages = [lc]

# Concat all languages (env + default locale),
#  and here we have the languages and location of the translations
#
languages = DEFAULT_LANGUAGES + languages + ["en_US"]
mo_location = LOCALE_DIR

# Lets tell those details to gettext
#  (nothing to change here for you)
gettext.install(True)
gettext.bindtextdomain(APP_NAME, mo_location)
gettext.textdomain(APP_NAME)
language = gettext.translation(
    APP_NAME, mo_location, languages=languages, fallback=True
)

_ = T = translator = language.gettext


# Setup pygubu translations
pygubu_app = gettext.translation(
    "pygubu", mo_location, languages=languages, fallback=True
)
pygubu_i18n.setup_translator(pygubu_app.gettext)
