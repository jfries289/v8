# Copyright 2013 the V8 project authors. All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#     * Neither the name of Google Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# This file is automatically generated from the V8 source and should not
# be modified manually, run 'make grokdump' instead to update this file.

# List of known V8 instance types.
INSTANCE_TYPES = {
  64: "STRING_TYPE",
  68: "ASCII_STRING_TYPE",
  65: "CONS_STRING_TYPE",
  69: "CONS_ASCII_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  71: "SLICED_ASCII_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  70: "EXTERNAL_ASCII_STRING_TYPE",
  74: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  82: "SHORT_EXTERNAL_STRING_TYPE",
  86: "SHORT_EXTERNAL_ASCII_STRING_TYPE",
  90: "SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  0: "INTERNALIZED_STRING_TYPE",
  4: "ASCII_INTERNALIZED_STRING_TYPE",
  1: "CONS_INTERNALIZED_STRING_TYPE",
  5: "CONS_ASCII_INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  6: "EXTERNAL_ASCII_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  18: "SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE",
  22: "SHORT_EXTERNAL_ASCII_INTERNALIZED_STRING_TYPE",
  26: "SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "MAP_TYPE",
  130: "CODE_TYPE",
  131: "ODDBALL_TYPE",
  132: "CELL_TYPE",
  133: "PROPERTY_CELL_TYPE",
  134: "HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "FREE_SPACE_TYPE",
  138: "EXTERNAL_INT8_ARRAY_TYPE",
  139: "EXTERNAL_UINT8_ARRAY_TYPE",
  140: "EXTERNAL_INT16_ARRAY_TYPE",
  141: "EXTERNAL_UINT16_ARRAY_TYPE",
  142: "EXTERNAL_INT32_ARRAY_TYPE",
  143: "EXTERNAL_UINT32_ARRAY_TYPE",
  144: "EXTERNAL_FLOAT32_ARRAY_TYPE",
  145: "EXTERNAL_FLOAT64_ARRAY_TYPE",
  146: "EXTERNAL_UINT8_CLAMPED_ARRAY_TYPE",
  147: "FIXED_INT8_ARRAY_TYPE",
  148: "FIXED_UINT8_ARRAY_TYPE",
  149: "FIXED_INT16_ARRAY_TYPE",
  150: "FIXED_UINT16_ARRAY_TYPE",
  151: "FIXED_INT32_ARRAY_TYPE",
  152: "FIXED_UINT32_ARRAY_TYPE",
  153: "FIXED_FLOAT32_ARRAY_TYPE",
  154: "FIXED_FLOAT64_ARRAY_TYPE",
  155: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  157: "FILLER_TYPE",
  158: "DECLARED_ACCESSOR_DESCRIPTOR_TYPE",
  159: "DECLARED_ACCESSOR_INFO_TYPE",
  160: "EXECUTABLE_ACCESSOR_INFO_TYPE",
  161: "ACCESSOR_PAIR_TYPE",
  162: "ACCESS_CHECK_INFO_TYPE",
  163: "INTERCEPTOR_INFO_TYPE",
  164: "CALL_HANDLER_INFO_TYPE",
  165: "FUNCTION_TEMPLATE_INFO_TYPE",
  166: "OBJECT_TEMPLATE_INFO_TYPE",
  167: "SIGNATURE_INFO_TYPE",
  168: "TYPE_SWITCH_INFO_TYPE",
  170: "ALLOCATION_MEMENTO_TYPE",
  169: "ALLOCATION_SITE_TYPE",
  171: "SCRIPT_TYPE",
  172: "CODE_CACHE_TYPE",
  173: "POLYMORPHIC_CODE_CACHE_TYPE",
  174: "TYPE_FEEDBACK_INFO_TYPE",
  175: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  176: "BOX_TYPE",
  179: "FIXED_ARRAY_TYPE",
  156: "FIXED_DOUBLE_ARRAY_TYPE",
  180: "CONSTANT_POOL_ARRAY_TYPE",
  181: "SHARED_FUNCTION_INFO_TYPE",
  182: "JS_MESSAGE_OBJECT_TYPE",
  185: "JS_VALUE_TYPE",
  186: "JS_DATE_TYPE",
  187: "JS_OBJECT_TYPE",
  188: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  189: "JS_GENERATOR_OBJECT_TYPE",
  190: "JS_MODULE_TYPE",
  191: "JS_GLOBAL_OBJECT_TYPE",
  192: "JS_BUILTINS_OBJECT_TYPE",
  193: "JS_GLOBAL_PROXY_TYPE",
  194: "JS_ARRAY_TYPE",
  195: "JS_ARRAY_BUFFER_TYPE",
  196: "JS_TYPED_ARRAY_TYPE",
  197: "JS_DATA_VIEW_TYPE",
  184: "JS_PROXY_TYPE",
  198: "JS_SET_TYPE",
  199: "JS_MAP_TYPE",
  200: "JS_WEAK_MAP_TYPE",
  201: "JS_WEAK_SET_TYPE",
  202: "JS_REGEXP_TYPE",
  203: "JS_FUNCTION_TYPE",
  183: "JS_FUNCTION_PROXY_TYPE",
  177: "DEBUG_INFO_TYPE",
  178: "BREAK_POINT_INFO_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  0x08081: (136, "ByteArrayMap"),
  0x080a9: (129, "MetaMap"),
  0x080d1: (131, "OddballMap"),
  0x080f9: (4, "AsciiInternalizedStringMap"),
  0x08121: (179, "FixedArrayMap"),
  0x08149: (134, "HeapNumberMap"),
  0x08171: (137, "FreeSpaceMap"),
  0x08199: (157, "OnePointerFillerMap"),
  0x081c1: (157, "TwoPointerFillerMap"),
  0x081e9: (132, "CellMap"),
  0x08211: (133, "GlobalPropertyCellMap"),
  0x08239: (181, "SharedFunctionInfoMap"),
  0x08261: (179, "NativeContextMap"),
  0x08289: (130, "CodeMap"),
  0x082b1: (179, "ScopeInfoMap"),
  0x082d9: (179, "FixedCOWArrayMap"),
  0x08301: (156, "FixedDoubleArrayMap"),
  0x08329: (180, "ConstantPoolArrayMap"),
  0x08351: (179, "HashTableMap"),
  0x08379: (128, "SymbolMap"),
  0x083a1: (64, "StringMap"),
  0x083c9: (68, "AsciiStringMap"),
  0x083f1: (65, "ConsStringMap"),
  0x08419: (69, "ConsAsciiStringMap"),
  0x08441: (67, "SlicedStringMap"),
  0x08469: (71, "SlicedAsciiStringMap"),
  0x08491: (66, "ExternalStringMap"),
  0x084b9: (74, "ExternalStringWithOneByteDataMap"),
  0x084e1: (70, "ExternalAsciiStringMap"),
  0x08509: (82, "ShortExternalStringMap"),
  0x08531: (90, "ShortExternalStringWithOneByteDataMap"),
  0x08559: (0, "InternalizedStringMap"),
  0x08581: (1, "ConsInternalizedStringMap"),
  0x085a9: (5, "ConsAsciiInternalizedStringMap"),
  0x085d1: (2, "ExternalInternalizedStringMap"),
  0x085f9: (10, "ExternalInternalizedStringWithOneByteDataMap"),
  0x08621: (6, "ExternalAsciiInternalizedStringMap"),
  0x08649: (18, "ShortExternalInternalizedStringMap"),
  0x08671: (26, "ShortExternalInternalizedStringWithOneByteDataMap"),
  0x08699: (22, "ShortExternalAsciiInternalizedStringMap"),
  0x086c1: (86, "ShortExternalAsciiStringMap"),
  0x086e9: (64, "UndetectableStringMap"),
  0x08711: (68, "UndetectableAsciiStringMap"),
  0x08739: (138, "ExternalInt8ArrayMap"),
  0x08761: (139, "ExternalUint8ArrayMap"),
  0x08789: (140, "ExternalInt16ArrayMap"),
  0x087b1: (141, "ExternalUint16ArrayMap"),
  0x087d9: (142, "ExternalInt32ArrayMap"),
  0x08801: (143, "ExternalUint32ArrayMap"),
  0x08829: (144, "ExternalFloat32ArrayMap"),
  0x08851: (145, "ExternalFloat64ArrayMap"),
  0x08879: (146, "ExternalUint8ClampedArrayMap"),
  0x088a1: (148, "FixedUint8ArrayMap"),
  0x088c9: (147, "FixedInt8ArrayMap"),
  0x088f1: (150, "FixedUint16ArrayMap"),
  0x08919: (149, "FixedInt16ArrayMap"),
  0x08941: (152, "FixedUint32ArrayMap"),
  0x08969: (151, "FixedInt32ArrayMap"),
  0x08991: (153, "FixedFloat32ArrayMap"),
  0x089b9: (154, "FixedFloat64ArrayMap"),
  0x089e1: (155, "FixedUint8ClampedArrayMap"),
  0x08a09: (179, "NonStrictArgumentsElementsMap"),
  0x08a31: (179, "FunctionContextMap"),
  0x08a59: (179, "CatchContextMap"),
  0x08a81: (179, "WithContextMap"),
  0x08aa9: (179, "BlockContextMap"),
  0x08ad1: (179, "ModuleContextMap"),
  0x08af9: (179, "GlobalContextMap"),
  0x08b21: (182, "JSMessageObjectMap"),
  0x08b49: (135, "ForeignMap"),
  0x08b71: (187, "NeanderMap"),
  0x08b99: (170, "AllocationMementoMap"),
  0x08bc1: (169, "AllocationSiteMap"),
  0x08be9: (173, "PolymorphicCodeCacheMap"),
  0x08c11: (171, "ScriptMap"),
  0x08c61: (187, "ExternalMap"),
  0x08cb1: (176, "BoxMap"),
  0x08cd9: (158, "DeclaredAccessorDescriptorMap"),
  0x08d01: (159, "DeclaredAccessorInfoMap"),
  0x08d29: (160, "ExecutableAccessorInfoMap"),
  0x08d51: (161, "AccessorPairMap"),
  0x08d79: (162, "AccessCheckInfoMap"),
  0x08da1: (163, "InterceptorInfoMap"),
  0x08dc9: (164, "CallHandlerInfoMap"),
  0x08df1: (165, "FunctionTemplateInfoMap"),
  0x08e19: (166, "ObjectTemplateInfoMap"),
  0x08e41: (167, "SignatureInfoMap"),
  0x08e69: (168, "TypeSwitchInfoMap"),
  0x08e91: (172, "CodeCacheMap"),
  0x08eb9: (174, "TypeFeedbackInfoMap"),
  0x08ee1: (175, "AliasedArgumentsEntryMap"),
  0x08f09: (177, "DebugInfoMap"),
  0x08f31: (178, "BreakPointInfoMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("OLD_POINTER_SPACE", 0x08081): "NullValue",
  ("OLD_POINTER_SPACE", 0x08091): "UndefinedValue",
  ("OLD_POINTER_SPACE", 0x080a1): "TheHoleValue",
  ("OLD_POINTER_SPACE", 0x080b1): "TrueValue",
  ("OLD_POINTER_SPACE", 0x080c1): "FalseValue",
  ("OLD_POINTER_SPACE", 0x080d1): "UninitializedValue",
  ("OLD_POINTER_SPACE", 0x080e1): "NoInterceptorResultSentinel",
  ("OLD_POINTER_SPACE", 0x080f1): "ArgumentsMarker",
  ("OLD_POINTER_SPACE", 0x08101): "NumberStringCache",
  ("OLD_POINTER_SPACE", 0x08909): "SingleCharacterStringCache",
  ("OLD_POINTER_SPACE", 0x08d11): "StringSplitCache",
  ("OLD_POINTER_SPACE", 0x09119): "RegExpMultipleCache",
  ("OLD_POINTER_SPACE", 0x09521): "TerminationException",
  ("OLD_POINTER_SPACE", 0x09531): "MessageListeners",
  ("OLD_POINTER_SPACE", 0x0954d): "CodeStubs",
  ("OLD_POINTER_SPACE", 0x0ca65): "MegamorphicSymbol",
  ("OLD_POINTER_SPACE", 0x0ca75): "UninitializedSymbol",
  ("OLD_POINTER_SPACE", 0x10ae9): "NonMonomorphicCache",
  ("OLD_POINTER_SPACE", 0x110fd): "PolymorphicCodeCache",
  ("OLD_POINTER_SPACE", 0x11105): "NativesSourceCache",
  ("OLD_POINTER_SPACE", 0x11155): "EmptyScript",
  ("OLD_POINTER_SPACE", 0x11189): "IntrinsicFunctionNames",
  ("OLD_POINTER_SPACE", 0x141a5): "ObservationState",
  ("OLD_POINTER_SPACE", 0x141b1): "FrozenSymbol",
  ("OLD_POINTER_SPACE", 0x141c1): "NonExistentSymbol",
  ("OLD_POINTER_SPACE", 0x141d1): "ElementsTransitionSymbol",
  ("OLD_POINTER_SPACE", 0x141e1): "EmptySlowElementDictionary",
  ("OLD_POINTER_SPACE", 0x1437d): "ObservedSymbol",
  ("OLD_POINTER_SPACE", 0x1438d): "AllocationSitesScratchpad",
  ("OLD_POINTER_SPACE", 0x14795): "MicrotaskState",
  ("OLD_POINTER_SPACE", 0x36241): "StringTable",
  ("OLD_DATA_SPACE", 0x08099): "EmptyDescriptorArray",
  ("OLD_DATA_SPACE", 0x080a1): "EmptyFixedArray",
  ("OLD_DATA_SPACE", 0x080a9): "NanValue",
  ("OLD_DATA_SPACE", 0x08141): "EmptyByteArray",
  ("OLD_DATA_SPACE", 0x08149): "EmptyConstantPoolArray",
  ("OLD_DATA_SPACE", 0x0828d): "EmptyExternalInt8Array",
  ("OLD_DATA_SPACE", 0x08299): "EmptyExternalUint8Array",
  ("OLD_DATA_SPACE", 0x082a5): "EmptyExternalInt16Array",
  ("OLD_DATA_SPACE", 0x082b1): "EmptyExternalUint16Array",
  ("OLD_DATA_SPACE", 0x082bd): "EmptyExternalInt32Array",
  ("OLD_DATA_SPACE", 0x082c9): "EmptyExternalUint32Array",
  ("OLD_DATA_SPACE", 0x082d5): "EmptyExternalFloat32Array",
  ("OLD_DATA_SPACE", 0x082e1): "EmptyExternalFloat64Array",
  ("OLD_DATA_SPACE", 0x082ed): "EmptyExternalUint8ClampedArray",
  ("OLD_DATA_SPACE", 0x082f9): "InfinityValue",
  ("OLD_DATA_SPACE", 0x08305): "MinusZeroValue",
  ("CODE_SPACE", 0x138e1): "JsConstructEntryCode",
  ("CODE_SPACE", 0x21361): "JsEntryCode",
}
