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


class IntentAPI(object):

    def create_intent(
        self,
        amount,
        currency,
        application_fee_amount=None,
        capture_method=None,
        confirm=None,
        description=None,
        automatic_payment_methods=None,
        three_d_secure=None,
        return_url=None,
        payment_method_types=[],
        payment_method_options={},
        metadata={},
    ):
        url = self.base_url + "payment_intents"
        params = {"amount": amount, "currency": currency}
        if application_fee_amount:
            params["application_fee_amount"] = application_fee_amount
        if capture_method:
            params["capture_method"] = capture_method
        if confirm:
            params["confirm"] = confirm
        if description:
            params["description"] = description
        if not automatic_payment_methods == None:
            params["automatic_payment_methods[enabled]"] = (
                "true" if automatic_payment_methods else "false"
            )
        if three_d_secure:
            params["payment_method_options[card][request_three_d_secure]"] = (
                three_d_secure
            )
        if return_url:
            params["return_url"] = return_url
        for payment_method_type in payment_method_types:
            params["payment_method_types[]"] = payment_method_type
        for key, value in payment_method_options.items():
            for _key, _value in value.items():
                params["payment_method_options[" + key + "][" + _key + "]"] = _value
        for key, value in metadata.items():
            params["metadata[" + key + "]"] = value
        contents = self.post(url, params=params)
        return contents

    def capture_intent(self, identifier):
        url = self.base_url + "payment_intents/%s/capture" % identifier
        contents = self.post(url)
        return contents

    def confirm_intent(self, identifier, return_url=None):
        url = self.base_url + "payment_intents/%s/confirm" % identifier
        params = {}
        if return_url:
            params["return_url"] = return_url
        contents = self.post(url, params=params)
        return contents
