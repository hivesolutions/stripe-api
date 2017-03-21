#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Stripe API
# Copyright (c) 2008-2017 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2017 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

class SourceApi(object):

    def create_card_source(
        self,
        exp_month,
        exp_year,
        number,
        type = "card",
        cvc = None,
        name = None,
        address_country = None,
        address_state = None,
        address_city = None,
        address_zip = None,
        address_line1 = None,
        address_line2 = None
    ):
        url = self.base_url + "sources"
        params = {
            "type" : type,
            "card[exp_month]" : exp_month,
            "card[exp_year]" : exp_year,
            "card[number]" : number
        }
        if cvc: params["card[cvc]"] = cvc
        if name: params["owner[name]"] = name
        if address_country: params["owner[address][country]"] = address_country
        if address_state: params["owner[address][state]"] = address_state
        if address_city: params["owner[address][city]"] = address_city
        if address_zip: params["owner[address][postal_code]"] = address_zip
        if address_line1: params["owner[address][line1]"] = address_line1
        if address_line2: params["owner[address][line2]"] = address_line2
        contents = self.post(url, params = params)
        return contents

    def create_3d_secure_source(
        self,
        amount,
        currency,
        return_url,
        type = "three_d_secure",
        card = None,
        customer = None
    ):
        url = self.base_url + "sources"
        params = {
            "amount" : amount,
            "currency" : currency,
            "type" : type,
            "redirect[return_url]" : return_url
        }
        if card: params["three_d_secure[card]"] = card
        if customer: params["three_d_secure[customer]"] = customer
        contents = self.post(url, params = params)
        return contents
