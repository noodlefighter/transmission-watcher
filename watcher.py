
import time
import os
import argparse

from transmission_rpc import *

# configs
host='192.168.0.142'
port=9091
username=''
password=''
base_watch_dir = '/path/to/watch_dir'
base_download_dir = '/downloads'
subdirs = [
    'anime',
    'movie',
    'music',
    'games',
    'others',
]
check_interval = 20 # seconds

def add_torrent(torrent_path, download_dir):
    global host, port, username, password
    with Client(host=host, port=port, username=username, password=password) as c:
        c.add_torrent("file://" + torrent_path, download_dir=download_dir)

def do_watch(watch_dir, download_dir):
    ls = os.listdir(watch_dir)
    if ls == []:
        return

    for filename in ls:
        if filename.lower().endswith('.torrent'):
            print('found torrent "{}" in "{}"'.format(filename, watch_dir))
            filepath = watch_dir + '/' + filename
            try:
                print('now add {} to task'.format(filename))
                add_torrent(filepath, download_dir)
                print('now rename "{}" to "{}.added"'.format(filename, filename))
                os.rename(filepath, filepath + '.added')
            except:
                print('Unexpected error')

parser = argparse.ArgumentParser()
parser.add_argument('--oneshot', action='store_true', help='just run a single time')
args = parser.parse_args()

while True:
    for d in subdirs:
        src_dir = base_watch_dir + '/' + d
        dst_dir = base_download_dir + '/' + d
        if os.path.exists(src_dir):
            do_watch(src_dir, dst_dir)

    if args.oneshot:
        break

    time.sleep(check_interval)
