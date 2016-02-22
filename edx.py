#!/usr/bin/env python
# encoding: utf-8

from fabric.api import local, cd, run, env, sudo, settings, prefix
from settings import hosts,password
#ssh要用到的参数
env.hosts = hosts
env.password = password



#本地命令
def local_hello():
    local('echo hello,$USER')
    #刚才的操作换到这里，你懂的

######################################

#远程命令（控制edx服务器）

##查看log 参数为最后的行数和log种类
##usage: fab -f fabric2.py tailLog:10,cms (打印最新的10条cms日志)
def tailLog(n=20, log="lms"):
    #with cd('~/temp'):   #cd用于进入某个目录
    sudo('sudo tail -n {n} /edx/var/log/{log}/edx.log'.format(n=n,
                                                              log=log)
         )  #远程操作用run


def shell():
    sudo(
        "sudo -u www-data /edx/bin/python.edxapp /edx/app/edxapp/edx-platform/manage.py lms --settings aws shell")

#run devstack to debug
def devstack(port="5000"):
    sudo(
        "sudo -u www-data /edx/bin/python.edxapp /edx/app/edxapp/edx-platform/manage.py lms runserver 0.0.0.0:5000 --settings devstack")

#show status
def status():
    sudo("sudo /edx/bin/supervisorctl status")


#restart edxapp
def restart_edxapp():
    sudo("sudo /edx/bin/supervisorctl restart edxapp:")


#paver update_assets
def update_assets(site="lms"):
    run("/edx/bin/edxapp-update-assets-{site}".format(site=site))

#paver update_assets
def watch_assets(site="lms"):
    #修改文件,需要远程执行代码
    sudo("rm /edx/bin/edxapp-watch-assets-{site}".format(site=site))
    sudo("cp /edx/bin/edxapp-update-assets-{site} /edx/bin/edxapp-watch-assets-{site}".format(site=site))
    sudo("sed -i 's/update_assets.*/& --debug --watch/' /edx/bin/edxapp-watch-assets-{site}".format(site=site))
    sudo("/edx/bin/edxapp-watch-assets-{site}".format(site=site))


#paver update_assets
def create_scss_maps(site="lms"):
    sudo("cp /edx/bin/edxapp-update-assets-{site} /edx/bin/create_scss_maps".format(site=site))
    sudo("sed -i 's/update_assets.*/& --debug/' /edx/bin/create_scss_maps")
    sudo("/edx/bin/create_scss_maps".format(site=site))
    sudo("rm /edx/bin/create_scss_maps")

def edxapp_pip(args="freeze"):
    run("/edx/bin/pip.edxapp {args}".format(args=args))

def install_notebook():
    #如果是cypress版需要先重装django-extensions
    sudo("/edx/bin/pip.edxapp install ipython[notebook]")

#添加css文件到课件页面
#def add_css_to_courseware_html(url="xxx"):
#    sudo("sed -i /edx/app/edxapp/edx-platform/lms/templates/courseware/courseware.html")

def test_file():
    sudo("echo hello > /tmp/a && cp /tmp/a /tmp/b && cat /tmp/b")
