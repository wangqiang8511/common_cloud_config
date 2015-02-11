import json
import yaml

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

def render_template(template_name, context):
    template = env.get_template(template_name)
    print template.render(**context)


def load_setting(setting_file):
    return yaml.load(open(setting_file, 'r')) 


def main(args):
    import os
    template_name = args[0]
    template_filename = template_name + ".tmpl"
    conf_filename = template_name + ".conf"
    if not os.path.isfile(template_filename) or not os.path.isfile(conf_filename):
        print "Template/Conf file does not exists"
        print "Check file %s" % template_filename
        print "Check file %s" % conf_filename
        return
    context = load_setting(conf_filename)
    render_template(template_filename, context)
    pass


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
