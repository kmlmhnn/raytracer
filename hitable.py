import abc

class Hitable(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def hit(self, ray, t_min, t_max, hit_record):
        return




