# (c) 2015 ACSONE SA/NV, Dhinesh D
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Internal Users - Inactive Sessions Timeout",
    'summary': """
        This module disable all inactive sessions since a given delay""",
    'author': "ACSONE SA/NV, "
              "Dhinesh D, "
              "Jesse Morgan, "
              "LasLabs, "
              "Odoo Community Association (OCA)"
              "Aquevix Solutions Pvt Ltd.",
    'maintainer': 'Aquevix Solutions Pvt Ltd.',
    'website': "http://www.github.com/Aquevix/server-auth",
    'category': 'Tools',
    'version': '12.1.0.0.0',
    'license': 'AGPL-3',
    'data': [
        'data/ir_config_parameter_data.xml'
    ],
    'installable': True,
}
