# Defines a common set of members and operations consistent with the language used in version
# 2.0 of OGC's SWE Common Data Model


class AbstractSimpleComponent:
    data_type: DataType
    ogc_property_list: SimpleComponent
    reference_frame: str = None
    axis_id: str = None
    quality: Quality = None
    nil_values = None

    def copyTo(self, other: AbstractSimpleComponent):
        super.copyTo(other)
        other.data_type = self.data_type

        if nil_values != None:
            other.nil_values = self.nil_values.copy()
        else:
            other.nil_values = None

        self.quality_list.copyTo(other.quality_list)
        other.reference_frame = self.reference_frame
        other.axis_id = self.axis_id

# TODO: Implement Base Classes from SWE Common UML Diagrams
