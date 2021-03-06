# Copyright (C) 2016 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

import os
import xml.etree.ElementTree

from ..package import Package


class ChocolateyParser():
    def __init__(self):
        pass

    def Parse(self, path):
        result = []

        for pagepath in os.listdir(path):
            if not pagepath.endswith(".xml"):
                continue

            root = xml.etree.ElementTree.parse(os.path.join(path, pagepath))

            for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
                pkg = Package()
                pkg.name = entry.find("{http://www.w3.org/2005/Atom}title").text
                pkg.fullversion = entry.find("{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties/{http://schemas.microsoft.com/ado/2007/08/dataservices}Version").text
                pkg.version = pkg.fullversion
                pkg.homepage = entry.find("{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}properties/{http://schemas.microsoft.com/ado/2007/08/dataservices}ProjectUrl").text
                pkg.comment = entry.find("{http://www.w3.org/2005/Atom}summary").text

                result.append(pkg)

        return result
