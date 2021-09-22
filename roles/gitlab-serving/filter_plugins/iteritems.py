from ansible.module_utils import six

class FilterModule(object):
    def filters(self):
        return {'iteritems': self.iteritems }
    def iteritems(self, dict):
        return [{'k': k, 'v': v} for k, v in six.iteritems(dict)]
