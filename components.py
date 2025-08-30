from enum import IntEnum


class Kind(IntEnum):
    Error                   = 0
    Off                     = 1
    On                      = 2
    Buffer1                 = 3
    Not                     = 4
    And                     = 5
    And3                    = 6
    Nand                    = 7
    Or                      = 8
    Or3                     = 9
    Nor                     = 10
    Xor                     = 11
    Xnor                    = 12
    Counter8                = 13
    VirtualCounter8         = 14
    Counter64               = 15
    VirtualCounter64        = 16
    Ram8                    = 17
    VirtualRam8             = 18
    DELETED_0               = 19
    DELETED_1               = 20
    DELETED_17              = 21
    DELETED_18              = 22
    Register8               = 23
    VirtualRegister8        = 24
    Register8Red            = 25
    VirtualRegister8Red     = 26
    Register8RedPlus        = 27
    VirtualRegister8RedPlus = 28
    Register64              = 29
    VirtualRegister64       = 30
    Switch8                 = 31
    Mux8                    = 32
    Decoder1                = 33
    Decoder3                = 34
    Constant8               = 35
    Not8                    = 36
    Or8                     = 37
    And8                    = 38
    Xor8                    = 39
    Equal8                  = 40
    DELETED_2               = 41
    DELETED_3               = 42
    Neg8                    = 43
    Add8                    = 44
    Mul8                    = 45
    Splitter8               = 46
    Maker8                  = 47
    Splitter64              = 48
    Maker64                 = 49
    FullAdder               = 50
    BitMemory               = 51
    VirtualBitMemory        = 52
    DELETED_10              = 53
    Decoder2                = 54
    Timing                  = 55
    NoteSound               = 56
    DELETED_4               = 57
    DELETED_5               = 58
    Keyboard                = 59
    FileLoader              = 60
    Halt                    = 61
    WireCluster             = 62
    LevelScreen             = 63
    Program8_1              = 64
    Program8_1Red           = 65
    DELETED_6               = 66
    DELETED_7               = 67
    Program8_4              = 68
    LevelGate               = 69
    Input1                  = 70
    LevelInput2Pin          = 71
    LevelInput3Pin          = 72
    LevelInput4Pin          = 73
    LevelInputConditions    = 74
    Input8                  = 75
    Input64                 = 76
    LevelInputCode          = 77
    LevelInputArch          = 78
    Output1                 = 79
    LevelOutput1Sum         = 80
    LevelOutput1Car         = 81
    DELETED_8               = 82
    DELETED_9               = 83
    LevelOutput2Pin         = 84
    LevelOutput3Pin         = 85
    LevelOutput4Pin         = 86
    Output8                 = 87
    Output64                = 88
    LevelOutputArch         = 89
    LevelOutputCounter      = 90
    DELETED_11              = 91
    Custom                  = 92
    VirtualCustom           = 93
    Program                 = 94
    DelayLine1              = 95
    VirtualDelayLine1       = 96
    Console                 = 97
    Shl8                    = 98
    Shr8                    = 99

    Constant64              = 100
    Not64                   = 101
    Or64                    = 102
    And64                   = 103
    Xor64                   = 104
    Neg64                   = 105
    Add64                   = 106
    Mul64                   = 107
    Equal64                 = 108
    LessU64                 = 109
    LessI64                 = 110
    Shl64                   = 111
    Shr64                   = 112
    Mux64                   = 113
    Switch64                = 114

    ProbeMemoryBit          = 115
    ProbeMemoryWord         = 116

    AndOrLatch              = 117
    NandNandLatch           = 118
    NorNorLatch             = 119

    LessU8                  = 120
    LessI8                  = 121

    DotMatrixDisplay        = 122
    SegmentDisplay          = 123

    Input16                 = 124
    Input32                 = 125

    Output16                = 126
    Output32                = 127

    DELETED_12              = 128
    DELETED_13              = 129
    DELETED_14              = 130
    DELETED_15              = 131
    DELETED_16              = 132

    Buffer8                 = 133
    Buffer16                = 134
    Buffer32                = 135
    Buffer64                = 136

    ProbeWireBit            = 137
    ProbeWireWord           = 138

    Switch1                 = 139

    Output1z                = 140
    Output8z                = 141
    Output16z               = 142
    Output32z               = 143
    Output64z               = 144

    Constant16              = 145
    Not16                   = 146
    Or16                    = 147
    And16                   = 148
    Xor16                   = 149
    Neg16                   = 150
    Add16                   = 151
    Mul16                   = 152
    Equal16                 = 153
    LessU16                 = 154
    LessI16                 = 155
    Shl16                   = 156
    Shr16                   = 157
    Mux16                   = 158
    Switch16                = 159
    Splitter16              = 160
    Maker16                 = 161
    Register16              = 162
    VirtualRegister16       = 163
    Counter16               = 164
    VirtualCounter16        = 165

    Constant32              = 166
    Not32                   = 167
    Or32                    = 168
    And32                   = 169
    Xor32                   = 170
    Neg32                   = 171
    Add32                   = 172
    Mul32                   = 173
    Equal32                 = 174
    LessU32                 = 175
    LessI32                 = 176
    Shl32                   = 177
    Shr32                   = 178
    Mux32                   = 179
    Switch32                = 180
    Splitter32              = 181
    Maker32                 = 182
    Register32              = 183
    VirtualRegister32       = 184
    Counter32               = 185
    VirtualCounter32        = 186

    LevelOutput8z           = 187

    Nand8                   = 188
    Nor8                    = 189
    Xnor8                   = 190
    Nand16                  = 191
    Nor16                   = 192
    Xnor16                  = 193
    Nand32                  = 194
    Nor32                   = 195
    Xnor32                  = 196
    Nand64                  = 197
    Nor64                   = 198
    Xnor64                  = 199

    Ram                     = 200
    VirtualRam              = 201
    RamLatency              = 202
    VirtualRamLatency       = 203

    RamFast                 = 204
    VirtualRamFast          = 205
    Rom                     = 206
    VirtualRom              = 207
    SolutionRom             = 208
    VirtualSolutionRom      = 209

    DelayLine8              = 210
    VirtualDelayLine8       = 211
    DelayLine16             = 212
    VirtualDelayLine16      = 213
    DelayLine32             = 214
    VirtualDelayLine32      = 215
    DelayLine64             = 216
    VirtualDelayLine64      = 217

    RamDualLoad             = 218
    VirtualRamDualLoad      = 219

    Hdd                     = 220
    VirtualHdd              = 221

    Network                 = 222

    Rol8                    = 223
    Rol16                   = 224
    Rol32                   = 225
    Rol64                   = 226
    Ror8                    = 227
    Ror16                   = 228
    Ror32                   = 229
    Ror64                   = 230

    IndexerBit              = 231
    IndexerByte             = 232

    DivMod8                 = 233
    DivMod16                = 234
    DivMod32                = 235
    DivMod64                = 236

    SpriteDisplay           = 237
    ConfigDelay             = 238

    Clock                   = 239

    LevelInput1             = 240
    LevelInput8             = 241
    LevelOutput1            = 242
    LevelOutput8            = 243

    Ashr8                   = 244
    Ashr16                  = 245
    Ashr32                  = 246
    Ashr64                  = 247

    Bidirectional1          = 248
    VirtualBidirectional1   = 249
    Bidirectional8          = 250
    VirtualBidirectional8   = 251
    Bidirectional16         = 252
    VirtualBidirectional16  = 253
    Bidirectional32         = 254
    VirtualBidirectional32  = 255
    Bidirectional64         = 256
    VirtualBidirectional64  = 257