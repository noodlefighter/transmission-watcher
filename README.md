# transmission-watcher

transmission multi folder watcher.

Example for a **torrent watch folder** and **download file folder**:

```
~ ᐅ tree /home/r/dl-watch
/home/r/dl-watch
├── anime
├── games
├── movie
└── music

~ ᐅ tree /home/r/download
/home/r/download
├── anime
├── games
├── movie
└── music
```

transmission-watcher will scan each sub-dir, if torrent exsits, add the task with corresponding download folder.

## install

```
$ cd transmission-watcher
$ virtualenv .
$ source ./bin/activate
$ pip install -r requirements.txt
```

## configure

Edit configs in `watcher.py`.

## usage

```
$ cd transmission-watcher
$ ./bin/python watcher.py
```


