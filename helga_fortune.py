import subprocess

from helga.plugins import command

@command('fortune', help='provide a fortune')
def fortune (client, channel, nick, message, cmd, args):
    if args:
        fortune_file = args[0]
    else:
        fortune_file = ''
    return subprocess.check_output(['fortune', '-s', fortune_file])
