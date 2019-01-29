import copy


class OgcPropertyImpl:
    _value = None
    _name = None
    _title = None
    _href = None
    _role = None
    _arc_role = None
    _nil_reason = None
    _href_resolver = None

    def __init__(self, name, value):
        self._name = name
        self._value = value

    def copy_to(self, other):
        if isinstance(other, OgcPropertyImpl):
            other = copy.deepcopy(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self.name = name

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_href(self):
        return self._href

    def set_href(self, href):
        self._href = href

    def has_href(self):
        return self._href is not None

    def get_role(self):
        return self._role

    def set_role(self, role):
        self._role = role

    def get_arc_role(self):
        return self._arc_role

    def set_arc_role(self, arc_role):
        self._arc_role = arc_role

    def get_nil_reason(self):
        return self._nil_reason

    def set_nil_reason(self, nil_reason):
        self._nil_reason = nil_reason

    def get_value(self):
        try:
            if self.has_href() and not self.has_value() and self._href_resolver is not None:
                self.resolve_href()
            return self._value
        except IOError:
            print("Cannot load property from href")

    def has_value(self):
        return self._value is not None

    def set_value(self, value):
        self._value = value

    def set_href_resolver(self, href_resolver):
        self._href_resolver = href_resolver

    def resolve_href(self):
        if self.has_value():
            return True

        assert self.has_href(), "Property must have an href"
        assert self._href_resolver is not None, "No href resolver is configured"

        ret = self._href_resolver.resolve_href()
        self._href_resolver = None

        return ret

    def get_target(self):
        return self.get_value()
