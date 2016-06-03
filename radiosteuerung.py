#!/usr/bin/python3

import subprocess
import bottle as b

DEAD = 0
PLAYING = 1
PAUSED = 2
STOPPED = 3
UNKNOWN = 4

def _run_mocp(switch):
    p = subprocess.Popen(['mocp', switch], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    (output, dummy) = p.communicate()
    return (output, p.returncode)

def get_state():
    r = _run_mocp('-i')
    if r[1] == 2:
        return DEAD
    else:
        for e in filter(lambda b: b.startswith(b'State: '), r[0].split(b'\n')):
            # iterating over one element at most is such a 2AM solution
            verb = e[7:]
            if verb == b'PLAY':
                return PLAYING
            elif verb == b'PAUSE':
                return PAUSED
            elif verb == b'STOP':
                return STOPPED
        return UNKNOWN

def cmd_start():
    _run_mocp('-S')

def cmd_play():
    _run_mocp('-p')

def cmd_stop():
    _run_mocp('-s')

@b.route('/')
def index():
    playstate = get_state() == PLAYING
    return b.template('radiosteuerung', playstate=playstate)

@b.route('/do/<cmd>')
def command(cmd):
    method = 'cmd_' + cmd
    # XXX: wrap these functions in a class, use getattr() instead
    if method in globals():
        globals()[method]()
        return 'OK'
    else:
        b.abort(404, 'Method not found')

if get_state() == DEAD:
    cmd_start()

b.TEMPLATE_PATH.insert(0, '/insertpathhere/') # location of template
#b.run(host='localhost', port=8088, debug=True) # not recommended
b.run(host='0.0.0.0', port=8088) 
