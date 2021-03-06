# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/vlan-group' resources
# =============================================


class NetVlangroupSchema(MetaParser):

    schema = {}


class NetVlangroup(NetVlangroupSchema):
    """ To F5 resource for /mgmt/tm/net/vlan-group
    """

    cli_command = "/mgmt/tm/net/vlan-group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
