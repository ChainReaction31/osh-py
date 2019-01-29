import collections


class OgcPropertyList:
    _properties = collections.OrderedDict()

    def add_property(self, name, ogc_property):
        # Check if name is taken
        # TODO: look into OGCPropertyImpl
        self._properties[name] = ogc_property
        return ogc_property


# TODO: Protect content of _properties
# TODO: emulate the other functionality of OGCPropertyList in osh-core

