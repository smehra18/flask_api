#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import environ
import flask_api

app = flask_api.app 
wsgi_app = app.wsgi_app

