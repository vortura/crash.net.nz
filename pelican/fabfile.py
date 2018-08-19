from fabric import task
from invoke import run as local

from patchwork.transfers import rsync

import os

# c.run path configuration (can be absolute or relative to fabfile)
deploy_path = 'output'

# Remote server configuration
production = 'burroughs.crash.net.nz'
dest_path = '/var/www/crash'

@task
def clean(c):
    if os.path.isdir(deploy_path):
        local('rm -rf {}'.format(deploy_path))
        local('mkdir {}'.format(deploy_path))

@task
def build(c):
    local('pelican -s pelicanconf.py')

@task
def rebuild(c):
    clean(c)
    build(c)

@task
def regenerate(c):
    local('pelican -r -s pelicanconf.py')

@task
def serve(c):
    local('cd {} && python -m SimpleHTTPServer'.format(deploy_path))

@task
def reserve(c):
    build()
    serve()

@task
def preview(c):
    local('pelican -s publishconf.py')

@task
def publish(c):
    local('pelican -s publishconf.py')
    rsync(c, deploy_path + '/', dest_path, exclude=".DS_Store", delete=True)
    #project.rsync_project(
        #remote_dir=dest_path,
        #exclude=".DS_Store",
        #c.run_dir=DEPLOY_PATH.rstrip('/') + '/',
    #)
