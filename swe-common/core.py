# Defines a common set of members and operations consistent with the language used in version
# 2.0 of OGC's SWE Common Data Model


class AbstractSimpleComponent:
    data_type: DataType
    ogc_property_list: SimpleComponent
    reference_frame: str = None
    axisID: str = None
    quality: Quality = None
    nil_values = None

# TODO: Implement Base Classes from SWE Common UML Diagrams
