import os
import sys
import colored
from colored import stylize
from dotenv import load_dotenv
from helpers.helpers import print_tabs
load_dotenv()

def list_commands():
    headers = ['Command', 'Description']
    print('\n')
    print('Available Subcommands')
    print('\n\n')

    commands = [
        ['words:cloud', 'Creates a wordcloud from latest propaganda tweets.'],
        ['words:rank', 'Ranks words from latest propaganda tweets.'],
    ]

    print_tabs(commands, headers, 'simple')
    print('\n\n')


def command_error(required={}, opt=None):
    if(not (required or opt)):
        print(stylize('Error: your command did not match any known programs. Closing...', colored.fg('red')))
        print('\n')
        return

    if (required):
        print(stylize('FAILED: Requires arguments: ', colored.fg('red')))
        for var, rules in required.items():
            print(stylize('({}) [{}] in position {}'.format(rules['type'], var, rules['pos']), colored.fg('red')))
        print('\n')
    if (opt):
        print(stylize('Optional arguments: ', colored.fg('yellow')))
        if (isinstance(opt, dict)):
            for var, typ in opt.items():
                print(stylize('({}) [{}]'.format(var, typ), colored.fg('yellow')))
        if (isinstance(opt, list)):
            for var in opt.items():
                print(stylize('[{}]'.format(var), colored.fg('yellow')))
            print('\n')


def parse_args(args, required=[], opt=[]):
    params = {}

    if (required):
        for req, rules in required.items():
            if ('=' in args[rules['pos']]):
                rv = args[rules['pos']].split('=')[1]
            else:
                rv = args[rules['pos']]

            params[req] = rv

    if (required and params == {}):
        command_error()
    if (opt):
        for var, rules in opt.items():
            in_args = [var == arg.split('=')[0] for arg in args]

            if (True in in_args):
                if (rules['type'] == bool):
                    if ('--' in var):
                        var = var.split('--')[1]
                    if ('=' in var):
                        argvalue = var.split('=')[1]
                    else:
                        argvalue = True

                    params[var] = argvalue
                    continue

                argvalue = args[in_args.index(True)].split('=')[1]

                if (rules['type'] == int):
                    if (isinstance(int(argvalue), int)):
                        params[var] = int(argvalue)
                        continue
                    else:
                        print(stylize(var+' must be of type '+str(rules['type']), colored.fg('red')))
                        sys.exit()

                params[var] = argvalue

    return params

def words_controller(subroutine, args):
    if (subroutine == 'cloud'):
        from labs.word_frequency.wordcloud import main
        main()

    if (subroutine == 'rank'):
        from labs.word_frequency.word_ranks import main
        main()


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab.settings')
    sys.argv.pop(0)

    args = [arg.strip() for arg in sys.argv]

    if (args[0] in ['h', '-h', 'help', '--help', 'ls', 'list',]):
        list_commands()
        return

    if (':' in args[0]):
        command = args.pop(0)
        program = command.split(':')[0] + '_controller'
        subroutine = command.split(':')[1]

        globals()[program](subroutine, args)
        return
    else:
        program = args.pop(0) + '_controller'

        globals()[program](args)
        return


if __name__ == '__main__':
    main()
