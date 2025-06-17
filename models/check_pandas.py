from odoo import models, api
from odoo.exceptions import UserError
import selenium 

class CheckPandasModule(models.AbstractModel):
    _name = 'check.pandas.module'
    _description = 'Check Pandas Module Before Installation'

    @api.model
    def _check_pandas_installed(self):
        try:
            import pandas  # noqa: F401
        except ImportError:
            raise UserError("The 'pandas' Python module is not installed. Please install it using `pip install pandas` before installing this module.")

    @api.model
    def _register_hook(self):
        self._check_pandas_installed()
