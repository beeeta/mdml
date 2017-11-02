import click
import os

run_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))

@click.group()
def cli():
    pass

@click.command()
@click.argument('-i','--input',default='md',help='input folder or file path')
@click.argument('-o','--onput',default='html',help='onput folder or file path')
def conv(input,output):
    pass