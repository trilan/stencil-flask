import os
from random import choice
from stencil.base import Stencil


class Flask(Stencil):

    source = 'template'
    help = 'create new Flask project'

    def fill_context(self, args):
        self.context['secret_key'] = self.generate_secret_key()
        self.context['app_name'] = os.path.basename(args.target)

    def generate_secret_key(self):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        return ''.join(choice(chars) for i in range(50))

    """
    def collect_resources(self):
        super(Flask, self).collect_resources()
        app_name = self.context['app_name']
        for name in self.resources.keys():
            if not name.startswith('project/'):
                continue
            resource = self.resources.pop(name)
            name = '{0}{1}'.format(app_name, name[7:])
            print name
            print '{}->{}'.format(resource, resource.target)
            print '\n'
            self.resources[name] = resource
    """
