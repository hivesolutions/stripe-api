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

import unittest

import appier

import stripe


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.api = stripe.API(api_key="secret")
        self.api.request = self._request
        self.requests = []

    def _request(self, method, url, **kwargs):
        self.requests.append((method, url, kwargs))
        return dict(object="balance", livemode=False)

    def _reject(self, method, url, **kwargs):
        self.requests.append((method, url, kwargs))
        raise appier.HTTPError(None, code=401, extended=False)

    def test_basic(self):
        self.assertEqual(1 + 1, 2)

    def test_ping(self):
        result = self.api.ping()
        self.assertEqual(result, dict(object="balance", livemode=False))
        method, url, kwargs = self.requests[0]
        self.assertEqual(method, appier.http.get)
        self.assertEqual(url, "https://api.stripe.com/v1/balance")
        self.assertEqual(kwargs["headers"], dict(Authorization="Bearer secret"))
        self.assertEqual(list(kwargs["params"].items()), [])

        # the verification is made against the configured base URL
        # and using the key that has been provided to the constructor
        api = stripe.API(base_url="https://stripe.hive.pt/v1/", api_key="other")
        api.request = self._request
        api.ping()
        _method, url, kwargs = self.requests[1]
        self.assertEqual(url, "https://stripe.hive.pt/v1/balance")
        self.assertEqual(kwargs["headers"], dict(Authorization="Bearer other"))

        # an invalid (or revoked) key is rejected by Stripe and that
        # error must reach the caller instead of being silenced
        self.api.request = self._reject
        self.assertRaises(appier.HTTPError, self.api.ping)
        self.assertEqual(len(self.requests), 3)
