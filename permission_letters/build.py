#!/usr/bin/env python

from jinja2 import Template
import pandas as pd
from subprocess import call
import os

def main():
    with open('template.tex') as f:
        template = f.read()
    env = Template(template)

    with open('deanLetter.tex') as f:
        template = f.read()
    dean = Template(template)

    with open('papers.txt') as f:
        papers = f.read().split('\n')

    df = pd.read_csv('co-authors.txt', sep=',', header=0)

    os.chdir('docs')
    filename = 'deanLetter'
    with open(filename + '.tex', 'w') as f:
        data = dean.render(papers=papers)
        f.write(data)
    call(["latexmk","-pdf",filename])
    call(["latexmk","-c",filename])
    call(["rm",filename+".tex"])

    for _, row in df.iterrows():

        co_authored = []
        for paper in papers:
            # this is not going to work for repeated last names
            if row.last_name in paper:
                co_authored.append(paper)

        if len(co_authored) == 0:
            raise ValueError('Could not find a paper for %s %s. There may be a'
                             ' typo or you might not have any publications '
                             ' with this author.'%
                             (row.first_name, row.last_name))

        filename = "%s_%s-permission"%(row.first_name, row.last_name)
        with open(filename + '.tex', 'w') as f:
            data = env.render(first_name=row.first_name,
                              last_name=row.last_name, papers=co_authored)
            f.write(data)
        call(["latexmk","-pdf",filename])
        call(["latexmk","-c",filename])
        call(["rm",filename+".tex"])

if __name__ == '__main__':
    main()