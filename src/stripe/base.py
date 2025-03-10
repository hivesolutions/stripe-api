#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Stripe API
# Copyright (c) 2008-2025 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2025 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import token
from . import charge
from . import intent
from . import secure
from . import source
from . import account
from . import balance
from . import customer

BASE_URL = "https://api.stripe.com/v1/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """


class API(
    appier.API,
    token.TokenAPI,
    intent.IntentAPI,
    charge.ChargeAPI,
    secure.SecureAPI,
    source.SourceAPI,
    account.AccountAPI,
    balance.BalanceAPI,
    customer.CustomerAPI,
):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.api_key = appier.conf("STRIPE_API_KEY", None)
        self.base_url = kwargs.get("base_url", BASE_URL)
        self.api_key = kwargs.get("api_key", self.api_key)

    def build(
        self,
        method,
        url,
        data=None,
        data_j=None,
        data_m=None,
        headers=None,
        params=None,
        mime=None,
        kwargs=None,
    ):
        auth = kwargs.pop("auth", True)
        if auth:
            headers["Authorization"] = "Bearer %s" % self.api_key
