import os
import debugpy
import click
from click_plugins import with_plugins
from pkg_resources import iter_entry_points
from src.testcli import Directory

def attach_debugger():
    debugpy.listen(("0.0.0.0", 5678))
    debugpy.wait_for_client()

enable_debugpy = os.environ.get('DEBUG', 'False')
if enable_debugpy == "True":
    attach_debugger()

@with_plugins(iter_entry_points("testcli.plugins"))
@click.group("testcli")
def testcli():
    """Entry point for testcli."""


@testcli.command("create")
@click.option("--name", "-n", help="name of the directory", required=True)
def create(name: str):
    """Create Directory"""
    Directory(name).create()


@testcli.command("delete")
@click.option("--name", "-n", help="name of the directory", required=True)
def delete(name: str):
    """Delete Directory"""
    Directory(name).delete()
