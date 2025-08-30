#!/usr/bin/env python3
import sys

import snappy
from seri import fields
from seri.serializers import Serializer

from components import Kind


def is_custom_component(_s, _n, _f, attrs, _data, _offset):
    return attrs["kind"] == Kind.Custom

def is_program_component(_s, _n, _f, attrs, _data, _offset):
    return attrs["kind"] in [Kind.Program8_1, Kind.Program8_4, Kind.Program]


# TODO Generalize Z-fields
class ZUInt8List(fields.DynamicList):
    def __init__(self, validator=None):
        super().__init__(fields.UInt8(), validator)
        self.length = self.element_field.length

    def deserialize(self, data: bytes) -> (list, int):
        offset = 0
        elements = []

        while True:
            sub_result = super().deserialize(data)
            data = data[sub_result[1]:]
            elements += sub_result[0]
            offset += sub_result[1]
            if elements[-1] == 0:
                return elements, offset


class TCGString(fields.EncodedLength):
    def __init__(self, *args, **kwargs):
        super().__init__(length_field = fields.UInt16(), element_field = fields.DynamicString(), *args, **kwargs)


class TCGPointSerialier(Serializer):
    x = fields.UInt16()
    y = fields.UInt16()


class TCGProgramSerializer(Serializer):
    key = fields.UInt64()
    name = TCGString()

class TCGComponentSerializer(Serializer):
    kind = fields.UInt16()
    position = fields.NestedSerializer(TCGPointSerialier())
    rotation = fields.UInt8()
    permanent_id = fields.UInt64()
    custom_string = TCGString()
    setting_1 = fields.UInt64()
    setting_2 = fields.UInt64()
    ui_order = fields.UInt16()
    custom_id = fields.UInt64(deserialize_predicate=is_custom_component)
    custom_displacement =  fields.NestedSerializer(TCGPointSerialier(), deserialize_predicate=is_custom_component)
    programs =  fields.EncodedLength(
        fields.UInt16(), fields.DynamicList(
            fields.NestedSerializer(TCGProgramSerializer()),
        ),
        deserialize_predicate=is_program_component,
    )


class TCGWireSerializer(Serializer):
    kind = fields.UInt8()
    color = fields.UInt8()
    comment = TCGString()
    path = fields.NestedSerializer(TCGPointSerialier())
    segments = ZUInt8List()


class TCGSerialier(Serializer):
    save_id = fields.UInt64()
    hub_id = fields.UInt32()
    gate = fields.UInt64()
    delay = fields.UInt64()
    menu_visible = fields.UInt8()
    clock_speed = fields.UInt32()
    dependencies = fields.EncodedLength(fields.UInt16(), fields.DynamicList(fields.UInt64()))
    description = TCGString()
    camera_position = fields.NestedSerializer(TCGPointSerialier())
    synced = fields.UInt8()
    campaign_bound = fields.UInt8()
    architecture_score = fields.UInt16()  # Not used by the game
    player_data = fields.EncodedLength(fields.UInt16(), fields.DynamicList(fields.UInt8()))
    hub_description = TCGString()
    components = fields.EncodedLength(fields.UInt64(), fields.DynamicList(fields.NestedSerializer(TCGComponentSerializer())))
    wires = fields.EncodedLength(fields.UInt64(), fields.DynamicList(fields.NestedSerializer(TCGWireSerializer())))


def main(argv):
    path = argv[1]  # TODO validate argument count
    with open(path, "rb") as src:
        game_version = src.read(1)
        assert game_version == b"\x06"
        compressed = src.read()
    decompressed = snappy.uncompress(compressed)

    attrs = TCGSerialier().deserialize(decompressed)
    print(attrs)


if __name__ == "__main__":
    main(sys.argv)
