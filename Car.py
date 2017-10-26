#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Car(object):
    make = ""
    model = ""
    mileage = ""
    service_date = ""

    def __init__(self, make, model, mileage, service_date):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.service_date = service_date