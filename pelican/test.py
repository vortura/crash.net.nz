from invoke import task

@task
def foo(c):
    c.run('pelican')
