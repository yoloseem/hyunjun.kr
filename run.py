from web.app import create_app
import sys


def get_option(opts, wrapper=lambda x: x, validator=lambda x: True,
               default=None):
    for opt in opts:
        try:
            i = sys.argv.index(opt)
        except ValueError:
            continue
        try:
            try:
                opt_value = wrapper(sys.argv[i+1])
            except:
                print u'Invalid argument value.'
                exit()
        except IndexError:
            print u'Invalid arguments list.'
            exit()
        if not validator(opt_value):
            print u'Invalid argument value.'
            exit()
        return opt_value
    return default


if __name__ == '__main__':
    app = create_app()
    host = get_option(['--host', '-H'], default='0.0.0.0')
    port = get_option(['--port', '-P'], int, lambda x: isinstance(x, int), 1002)
    app.run(host=host, port=port)
