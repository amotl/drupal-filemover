import os
import argparse
import urllib

"""
example usage::

    dfm-move     --file=var/2010.txt sites/default/files/ sites/default/files/2010/
    dfm-updatedb --file=var/2010.txt sites/default/files/ sites/default/files/2010/
"""

def scan():
    pass


def move():
    args = get_args()
    source = args.source
    target = args.target

    print 'mkdir -p {target}'.format(**locals())
    for entry in read_filenames(args.file):
        cmd = get_move_command(source, target, entry)
        print cmd

def updatedb():
    """
    .. seealso::

        http://www.midwesternmac.com/blogs/geerlingguy/moving-your-drupal-files-folder-dev-live-sites
    """
    args = get_args()
    source = args.source
    target = args.target

    specs = [
        # Update the files table (which is used by the system as well as imagecache):
        {'tablename': 'files', 'fieldname': 'filepath'},

        # Update the boxes table (which is used for all the block content):
        {'tablename': 'boxes', 'fieldname': 'body'},

        # Update the node_revisions table (all the node content is in here... you'll need to update both the body and the teaser fields):
        {'tablename': 'node_revisions', 'fieldname': 'body'},
        {'tablename': 'node_revisions', 'fieldname': 'teaser'},

        # Update the users table 'picture' value (if you're using user pictures):
        {'tablename': 'users', 'fieldname': 'picture'},
    ]

    for spec in specs:
        for entry in read_filenames(args.file):
            sql = get_updatedb_line(spec['tablename'], spec['fieldname'], source, target, entry)
            print sql


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file', type=str, help='file containing the list of filenames to move')
    parser.add_argument(
        'source', type=str, help='the source folder, e.g. sites/OLDDOMAIN/files/')
    parser.add_argument(
        'target', type=str, help='the target folder, e.g. sites/NEWDOMAIN/files/')
    args = parser.parse_args()
    return args

def read_filenames(filename):
    with file(filename) as f:
        for line in f.readlines():
            yield os.path.basename(line.strip())

def get_updatedb_line(tablename, fieldname, source, target, filename):
    source = os.path.join(source, filename)
    target = os.path.join(target, filename)
    tpl = "UPDATE `{tablename}` SET `{fieldname}` = REPLACE(`{fieldname}`, '{source}', '{target}');"
    
    sql1 = tpl.format(**locals())

    source = urllib.quote(source)
    target = urllib.quote(target)
    sql2 = tpl.format(**locals())

    if sql1 == sql2:
        return sql1
    else:
        return sql1 + '\n' + sql2

def get_move_command(source, target, filename):
    source = os.path.join(source, filename)
    tpl = "mv '{source}' '{target}'"
    return tpl.format(**locals())
