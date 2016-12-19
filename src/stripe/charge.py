#!/usr/bin/python
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

class ChargeApi(object):

    def create_charge(
        self,
        amount,
        currency,
        exp_month,
        exp_year,
        number,
        cvc = None,
        name = None,
        description = None,
        statement_descriptor = None,
        address_country = None,
        address_state = None,
        address_city = None,
        address_zip = None,
        address_line1 = None,
        address_line2 = None,
        metadata = {}
    ):
        url = self.base_url + "charges"
        params = {
            "amount" : amount,
            "currency" : currency,
            "source[object]" : "card",
            "source[exp_month]" : exp_month,
            "source[exp_year]" : exp_year,
            "source[number]" : number
        }
        if cvc: params["source[cvc]"] = cvc
        if name: params["source[name]"] = name
        if description: params["description"] = description
        if statement_descriptor: params["statement_descriptor"] = statement_descriptor[:22]
        if address_country: params["source[address_country]"] = address_country
        if address_state: params["source[address_state]"] = address_state
        if address_city: params["source[address_city]"] = address_city
        if address_zip: params["source[address_zip]"] = address_zip
        if address_line1: params["source[address_line1]"] = address_line1
        if address_line2: params["source[address_line2]"] = address_line2
        for key, value in metadata.items():
            params["metadata[" + key + "]"] = value
        contents = self.post(url, params = params)
        return contents

    def create_charge_token(
        self,
        amount,
        currency,
        token,
        description = None,
        statement_descriptor = None,
        address_country = None,
        address_state = None,
        address_city = None,
        address_zip = None,
        address_line1 = None,
        address_line2 = None,
        metadata = {}
    ):
        url = self.base_url + "charges"
        params = {
            "amount" : amount,
            "currency" : currency,
            "source" : token
        }
        if description: params["description"] = description
        if statement_descriptor: params["statement_descriptor"] = statement_descriptor[:22]
        if address_country: params["source[address_country]"] = address_country
        if address_state: params["source[address_state]"] = address_state
        if address_city: params["source[address_city]"] = address_city
        if address_zip: params["source[address_zip]"] = address_zip
        if address_line1: params["source[address_line1]"] = address_line1
        if address_line2: params["source[address_line2]"] = address_line2
        for key, value in metadata.items():
            params["metadata[" + key + "]"] = value
        contents = self.post(url, params = params)
        return contents

    def get_charge(self, charge):
        url = self.base_url + "charges/%s" % charge
        contents = self.get(url)
        return contents
