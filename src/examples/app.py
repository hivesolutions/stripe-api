##!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Stripe API
# Copyright (c) 2008-2016 Hive Solutions Lda.
#
# This file is part of Hive Stripe API.
#
# Hive Stripe API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Stripe API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Stripe API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2016 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base

class StripeApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "stripe",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.balance()

    @appier.route("/balance", "GET")
    def balance(self):
        api = self.get_api()
        balance = api.get_balance()
        return balance

    @appier.route("/customers/new", "GET")
    def new_customer(self):
        api = self.get_api()
        balance = api.create_customer()
        return balance

    @appier.route("/customers/<str:id>/card/new", "GET")
    def new_card_customer(self, id):
        exp_month = self.field("exp_month", 1)
        exp_year = self.field("exp_year", 2020)
        number = self.field("number", 4242424242424242)
        api = self.get_api()
        balance = api.create_card_customer(
            id, exp_month, exp_year, number
        )
        return balance

    @appier.route("/charges/new", "GET")
    def new_charge(self):
        amount = self.field("amount", 100, cast = int)
        currency = self.field("currency", "EUR")
        exp_month = self.field("exp_month", 1)
        exp_year = self.field("exp_year", 2020)
        number = self.field("number", 4242424242424242)
        cvc = self.field("cvc", None)
        name = self.field("name", None)
        api = self.get_api()
        balance = api.create_charge(
            amount,
            currency,
            exp_month,
            exp_year,
            number,
            cvc = cvc,
            name = name
        )
        return balance

    @appier.route("/charges/<str:id>", "GET")
    def get_charge(self, id):
        api = self.get_api()
        charge = api.get_charge(id)
        return charge

    @appier.route("/tokens/new", "GET")
    def new_token(self):
        exp_month = self.field("exp_month", 1)
        exp_year = self.field("exp_year", 2020)
        number = self.field("number", 4242424242424242)
        cvc = self.field("cvc", None)
        name = self.field("name", None)
        api = self.get_api()
        token = api.create_token(
            exp_month, exp_year, number, cvc = cvc, name = name
        )
        return token

    @appier.route("/3d_secure/new", "GET")
    def new_3d_secure(self):
        amount = self.field("amount", 100, cast = int)
        currency = self.field("currency", "EUR")
        return_url = self.field("return_url", None)
        exp_month = self.field("exp_month", 1)
        exp_year = self.field("exp_year", 2020)
        number = self.field("number", 4242424242424242)
        cvc = self.field("cvc", None)
        name = self.field("name", None)
        api = self.get_api()
        return_url = return_url or self.url_for(
            "stripe.return_3d_secure",
            absolute = True
        )
        token = api.create_token(
            exp_month, exp_year, number, cvc = cvc, name = name
        )
        secure = api.create_3d_secure(
            amount,
            currency,
            return_url,
            card = token["id"]
        )
        return secure

    @appier.route("/3d_secure/redirect", "GET")
    def redirect_3d_secure(self):
        redirect_url = self.field("redirect_url", None)
        return self.html("<html>" +\
            "<body onload=\"document.autoRedirect.submit();\">" +\
            "<form name=\"autoRedirect\" method=\"POST\" action=\"%s\">" % redirect_url +\
            "</form>" +\
            "</body>" +\
            "</html>")

    @appier.route("/3d_secure/return", "GET")
    def return_3d_secure(self):
        status = self.field("status", "success")
        error_code = self.field("error_code", None)
        return dict(
            status = status,
            error_code = error_code
        )

    def get_api(self):
        return base.get_api()

if __name__ == "__main__":
    app = StripeApp()
    app.serve()
