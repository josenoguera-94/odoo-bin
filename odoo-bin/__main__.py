#!/usr/bin/env python3

# set server timezone in UTC before time module imported
__import__('os').environ['TZ'] = 'UTC'
from . import odoo

if __name__ == "__main__":
    odoo.cli.main()
