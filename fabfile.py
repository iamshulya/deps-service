# -*- coding: utf-8 -*-

from fabric.api import *
env.hosts = ['s-kh-fs1.msk.csat.ru']
env.user = 'shulgin'
env.password = ''
env.cwd = '/service/'


def mkdir_p(path):  # Создает директории
    run('mkdir -p ' + path)


def mkdir_p_local(path):  # Создает директории
    local('mkdir -p ' + path)
