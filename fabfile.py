# -*- coding: utf-8 -*-
import os
from fabric.api import *
from fabric.contrib.files import exists
env.hosts = ['server.domain.ru']  # Сервер
env.user = 'user'  # Пользователь
env.password = 'password'  # Пароль
env.cwd = '/service/'  # Домашняя директория
preCommand = 'service example stop'  # Команда выполняемая перед заменой файлов
postCommand = 'service example start'  # Команда выполняемая после замены файлов
newFolder = 'new'  # Локальная папка с новыми файлами
bupFolder = 'bup'  # Локальная папка для бэкапов с удаленного сервера


def mkdir_p(path):  # Создает директории на удаленной машине
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
    return(pathToFiles)


def do():
    run(preCommand)
    rFileList = listdir(newFolder)
    for rFile in rFileList:
        head, tail = os.path.split(env.cwd + rFile[len(newFolder) + 1:])
        headBup, tailBup = os.path.split(bupFolder + "/" + rFile[len(newFolder) + 1:])
        if exists(rFile[len(newFolder) + 1:]):
            if not os.path.isdir(headBup):
                mkdir_p_local(headBup)
            get(rFile[len(newFolder) + 1:], headBup)
        if not exists(head):
            mkdir_p(head)
        put(rFile, rFile[len(newFolder) + 1:])
    run(postCommand)


def undo():
    run(preCommand)
    rFileList = listdir(bupFolder)
    rFileListNew = listdir(newFolder)
    for rFileNew in rFileListNew:  # Удалить файлы кот. есть в папке new на удаленной машине
        run('rm -f ' + rFileNew[len(newFolder) + 1:])
    for rFile in rFileList:
        head, tail = os.path.split(env.cwd + rFile[len(bupFolder) + 1:])
        if not exists(head):
            mkdir_p(head)
        put(rFile, rFile[len(bupFolder) + 1:])
    run(postCommand)





