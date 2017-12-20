"""codex - VSCode Extension Manager

Usage:
    codex search <keyword>...
    codex install <extension-id>...
    codex uninstall <extension-id>...
    codex update [<extension-id>...]
    codex list [--show-versions]
    codex (-h | --help)
"""

from docopt import docopt

from . import core


def main():
    args = docopt(__doc__)

    if args['search']:
        query = ' '.join(args['<keyword>'])
        core.search(query)

    elif args['install']:
        for extension_id in args['<extension-id>']:
            core.install(extension_id)

    elif args['uninstall']:
        for extension_id in args['<extension-id>']:
            core.uninstall(extension_id)

    elif args['update']:
        core.update(args['<extension-id>'])

    elif args['list']:
        core.list_installed(args['--show-versions'])


if __name__ == '__main__':
    main()
