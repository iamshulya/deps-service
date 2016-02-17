# -*- coding: utf-8 -*-
from fabric.api import *

preCommand = '/etc/init.d/jetty stop'
postCommand = '/etc/init.d/jetty start'
service_root = '/service'
local_releases_root = 'releases'
env.user = 'deps'  # Пользователь
env.key_filename = './id_rsa'
