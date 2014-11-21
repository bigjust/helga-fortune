from helga.plugins import command

@command('fortune', help='provide a fortune')
def fortune (client, channel, nick, message, cmd, args):
    return 'Success!'
