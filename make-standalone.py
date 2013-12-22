import re
import sys

def read_input():
    return open('index.html', 'r').read()

def write_output(s):
    with open("index-standalone.html", "w") as f:
        f.write(s)

def read_config():
    return open('config.json', 'r').read()

def read_life():
    return open('life.md', 'r').read()

def replace_block(s, block_regex, content):
    reo = re.compile(block_regex, re.DOTALL)
    mo = mo = reo.search(s)
    if not mo:
        print "this is fishy -- could not find replacement block"
        sys.exit(1)
    m = mo.group(0)
    print m
    # this lamda makes python behave
    # http://stackoverflow.com/a/14576905/2536029
    return reo.sub(lambda _:content, s)

def hardcode_config(s):
    rep = "fn( %s );" % read_config()
    return replace_block(s, '..STANDALONE-CONFIG-START.*..STANDALONE-CONFIG-END', rep)

def hardcode_life(s):
    lines = read_life().split('\n')
    lines = [line.rstrip() for line in lines]
    lines = [line + "\\n\\" for line in lines]
    payload = "\n".join(lines)

    rep = 'fn( " %s     " );' % payload
    return replace_block(s, '..STANDALONE-LIFE-START.*..STANDALONE-LIFE-END', rep)

def main():
    s = read_input()
    s = hardcode_config(s)
    s = hardcode_life(s)
    write_output(s)

if __name__ == '__main__':
    main()
