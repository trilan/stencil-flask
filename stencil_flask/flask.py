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
