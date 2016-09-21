#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/TagDemo/")

from TagDemo import tagdemo as application
application.debug = True
application.secret_key = 'pepe2016'
