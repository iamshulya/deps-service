# -*- coding: utf-8 -*-
import os
from fabric.api import *
from fabric.contrib.files import exists
env.hosts = ['s-kh-fs1.msk.csat.ru']
env.user = 'shulgin'
env.password = 'Gbnth88'
env.cwd = '/service/'
preCommand = '/usr/bin/uptime'
postCommand = '/bin/hostname'


def mkdir_p(path):  # Создает директории
    run('mkdir -p ' + path)


def mkdir_p_local(path):  # Создает директории на локальной машине
    local('mkdir -p ' + path)


def listdir(path):  # Выдает список файлов/директорий
    pathToFiles = []
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            pathToFiles.append(os.path.join(dirname, filename))
        if '.git' in dirnames:
            dirnames.remove('.git')
    print(pathToFiles)








def check_file(path):
    if exists(path):
        print("Exists!")
    else:
        print("Not exists!")


def preDeploy(preCommand='/usr/bin/uptime'):
    sudo(preCommand)


