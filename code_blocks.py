import os
import re
from sys import stdout

import argh

@argh.arg('markdown-file', type=open)
@argh.arg('--output', choices=['files', 'stdout'])
@argh.arg('--output-dir', type=str)
def output_code_blocks(markdown_file, output='files', output_dir='examples'):
    if output == 'files':
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    in_block = False
    last_heading = None
    idx = 0

    for l in markdown_file.readlines():
        if l.startswith('#'):
            last_heading = l.strip()
            in_block = False
        elif l.startswith('    !python'):
            in_block = True
            filename = re.sub('[ -\/]+', '_', last_heading[1:].strip().lower())
            idx += 1
            filename = '{0:02d}'.format(idx) + '_' + filename + '.py'

            if output == 'files':
                code_file = open(os.path.join(output_dir, filename), 'w')
            else:
                print(filename)

        elif in_block and (len(l.strip()) == 0 or l.startswith('    ')):
            out = code_file if output == 'files' else stdout
            out_l = re.sub('^    ', '', l)
            print(out_l, end='', file=out)
        else:
            if in_block:
                code_file.close()

            in_block = False


if __name__ == '__main__':
    argh.dispatch_command(output_code_blocks)
