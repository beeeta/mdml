import click
import os
import markdown
import shutil

run_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))

@click.group()
def cli():
    pass

@cli.command()
@click.option('-i','--input',default='md',help='input folder or file path')
@click.option('-o','--outputdir',default='html',help='onput folder or file path')
def conv(input,outputdir):
    if not os.path.isabs(outputdir):
        outputdir = os.path.join(run_path,outputdir)
    if not os.path.isabs(input):
        input = os.path.join(run_path,input)
    do_conv(input,outputdir)

def do_conv(inputfile,outputdir):
    # file
    if os.path.isfile(inputfile):
        # 文件拷贝或者转换
        do_conv_file(inputfile=inputfile, outputdir=outputdir)
    else:
        # dir
        subfiles = os.listdir(inputfile)
        for subfile in subfiles:
            infile = os.path.join(inputfile, subfile)
            outfile = os.path.join(outputdir, os.path.basename(inputfile))
            do_conv(infile, outfile)


def do_conv_file(inputfile,outputdir,code='utf8'):
    md = markdown.Markdown()
    inputname = os.path.basename(inputfile)
    index = inputname.index('.md')
    if index:
        outputfile = os.path.join(outputdir,inputname[:index]+'.html')
        outputdir = os.path.dirname(outputfile)
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)
        open(outputfile,'w').close()
        md.convertFile(inputfile,outputfile,code)
    else:
        shutil.copy(inputfile,os.path.join(outputdir,inputname))
