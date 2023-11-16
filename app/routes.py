#!/usr/bin/env python3                  # add the shybang
# -*- coding: utf8 -*-                  #
"""Sample hello world Flask app"""

from flask import Flask                 # from the flask module import the Flask class

# OOP
app = Flask(__name__)                   # Create an instance of Flask into app
                                        # app now becomes an "object"

@app.get("/aboutme")                  # Flask decorate to map routes to "view function"
def aboutme():                          # Our function, in flask is a "view function"
    me = {                              # Python dictionary. Dictionaries are key-value pairs.
        "first_name": "Samantha",
        "last_name": "Roman",
        "hobbies": "Shopping",
        "is_active": True
    }
    return me                           # In flask, when you return a dictionary, if all
                                        # the fields are compatible with JSON,
                                        # it will be automatically converted into JSON for you.


@app.route("/products")
def products():
    product_list = ["Apples", "Oranges", "Bananas"]
    bullet_list = "".join(
        "<li>%s</li>" % product for product in product_list
        )
    return "<ul>%s</ul>" % bullet_list
