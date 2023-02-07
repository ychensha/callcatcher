#!/usr/bin/env python3
import os.path

cachedir = os.getenv('CATCHER_CACHE_DIR', os.path.expanduser('~/.callcatcher'))

def cachefile(file):
	file = os.path.realpath(file)
	file = cachedir + file
	return file
