@task
def audit(tsk):
    """
    Run audit check on the dependent packages
    """
    cmd = "safety check --full-report"
    tsk.run(cmd, echo=True, pty=True)


@task
def staticcheck(tsk):
    """
    Run static check on the projects files
    """
    cmd = "mypy ai21 tests"
    tsk.run(cmd, echo=True, pty=True)


@task
def isort(tsk):
    """
    Run static check on the projects files
    """
    cmd = "isort ai21 tests"
    tsk.run(cmd, echo=True, pty=True)
