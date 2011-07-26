
from .structures import DEVPROPKEY, BYTE

DEVPKEY_NAME = DEVPROPKEY.create(
    Data1=0xb725f130,
    Data2=0x47ef,
    Data3=0x101a,
    Data4=[0xa5, 0xf1, 0x02, 0x60, 0x8c, 0x9e, 0xeb, 0xac],
    pid=10)

DEVPKEY_Device_DeviceDesc = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=2)

DEVPKEY_Device_HardwareIds = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=3) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_CompatibleIds = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=4) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_Service = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=6) # DEVPROP_TYPE_STRING

DEVPKEY_Device_Class = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=9) # DEVPROP_TYPE_STRING

DEVPKEY_Device_ClassGuid = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=10) # DEVPROP_TYPE_GUID

DEVPKEY_Device_Driver = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=11) # DEVPROP_TYPE_STRING

DEVPKEY_Device_ConfigFlags = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=12) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_Manufacturer = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=13) # DEVPROP_TYPE_STRING

DEVPKEY_Device_FriendlyName = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=14) # DEVPROP_TYPE_STRING

DEVPKEY_Device_LocationInfo = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=15) # DEVPROP_TYPE_STRING

DEVPKEY_Device_PDOName = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=16) # DEVPROP_TYPE_STRING

DEVPKEY_Device_Capabilities = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=17) # DEVPROP_TYPE_UNINT32

DEVPKEY_Device_UINumber = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=18) # DEVPROP_TYPE_STRING

DEVPKEY_Device_UpperFilters = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=19) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_LowerFilters = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=20) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_BusTypeGuid = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=21) # DEVPROP_TYPE_GUID

DEVPKEY_Device_LegacyBusType = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=22) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_BusNumber = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=23) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_EnumeratorName = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=24) # DEVPROP_TYPE_STRING

DEVPKEY_Device_Security = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=25) # DEVPROP_TYPE_SECURITY_DESCRIPTOR

DEVPKEY_Device_SecuritySDS = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=26) # DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING

DEVPKEY_Device_DevType = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=27) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_Exclusive = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=28) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_Device_Characteristics = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=29) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_Address = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=30) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_UINumberDescFormat = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=31) # DEVPROP_TYPE_STRING

DEVPKEY_Device_PowerData = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=32) # DEVPROP_TYPE_BINARY

DEVPKEY_Device_RemovalPolicy = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=33) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_RemovalPolicyDefault = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=34) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_RemovalPolicyOverride = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=35) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_InstallState = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=36) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_LocationPaths = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=37) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_BaseContainerId = DEVPROPKEY.create(
    Data1=0xa45c254e,
    Data2=0xdf1c,
    Data3=0x4efd,
    Data4=[0x80, 0x20, 0x67, 0xd1, 0x46, 0xa8, 0x50, 0xe0],
    pid=38) # DEVPROP_TYPE_GUID


DEVPKEY_Device_DevNodeStatus = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=2) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_ProblemCode = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=3) # DEVPROP_TYPE_UINT32


DEVPKEY_Device_EjectionRelations = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=4) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_RemovalRelations = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=5) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_PowerRelations = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=6) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_BusRelations = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=7) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_Parent = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=8) # DEVPROP_TYPE_STRING

DEVPKEY_Device_Children = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=9) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_Siblings = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=10) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_TransportRelations = DEVPROPKEY.create(
    Data1=0x4340a6c5,
    Data2=0x93fa,
    Data3=0x4706,
    Data4=[0x97, 0x2c, 0x7b, 0x64, 0x80, 0x08, 0xa5, 0xa7],
    pid=11) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_Reported = DEVPROPKEY.create(
    Data1=0x80497100,
    Data2=0x8c73,
    Data3=0x48b9,
    Data4=[0xaa, 0xd9, 0xce, 0x38, 0x7e, 0x19, 0xc5, 0x6e],
    pid=2) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_Device_Legacy = DEVPROPKEY.create(
    Data1=0x80497100,
    Data2=0x8c73,
    Data3=0x48b9,
    Data4=[0xaa, 0xd9, 0xce, 0x38, 0x7e, 0x19, 0xc5, 0x6e],
    pid=3) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_Device_InstanceId = DEVPROPKEY.create(
    Data1=0x78c34fc8,
    Data2=0x104a,
    Data3=0x4aca,
    Data4=[0x9e, 0xa4, 0x52, 0x4d, 0x52, 0x99, 0x6e, 0x57],
    pid=256) # DEVPROP_TYPE_STRING

DEVPKEY_Device_ContainerId = DEVPROPKEY.create(
    Data1=0x8c7ed206,
    Data2=0x3f8a,
    Data3=0x4827,
    Data4=[0xb3, 0xab, 0xae, 0x9e, 0x1f, 0xae, 0xfc, 0x6c],
    pid=2) # DEVPROP_TYPE_GUID

DEVPKEY_Device_ModelId = DEVPROPKEY.create(
    Data1=0x80d81ea6,
    Data2=0x7473,
    Data3=0x4b0c,
    Data4=[0x82, 0x16, 0xef, 0xc1, 0x1a, 0x2c, 0x4c, 0x8b],
    pid=2) # DEVPROP_TYPE_GUID

DEVPKEY_Device_FriendlyNameAttributes = DEVPROPKEY.create(
    Data1=0x80d81ea6,
    Data2=0x7473,
    Data3=0x4b0c,
    Data4=[0x82, 0x16, 0xef, 0xc1, 0x1a, 0x2c, 0x4c, 0x8b],
    pid=3) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_ManufacturerAttributes = DEVPROPKEY.create(
    Data1=0x80d81ea6,
    Data2=0x7473,
    Data3=0x4b0c,
    Data4=[0x82, 0x16, 0xef, 0xc1, 0x1a, 0x2c, 0x4c, 0x8b],
    pid=4) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_PresenceNotForDevice = DEVPROPKEY.create(
    Data1=0x80d81ea6,
    Data2=0x7473,
    Data3=0x4b0c,
    Data4=[0x82, 0x16, 0xef, 0xc1, 0x1a, 0x2c, 0x4c, 0x8b],
    pid=5) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_Numa_Proximity_Domain = DEVPROPKEY.create(
    Data1=0x540b947e,
    Data2=0x8b40,
    Data3=0x45bc,
    Data4=[0xa8, 0xa2, 0x6a, 0x0b, 0x89, 0x4c, 0xbd, 0xa2],
    pid=1) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_DHP_Rebalance_Policy = DEVPROPKEY.create(
    Data1=0x540b947e,
    Data2=0x8b40,
    Data3=0x45bc,
    Data4=[0xa8, 0xa2, 0x6a, 0x0b, 0x89, 0x4c, 0xbd, 0xa2],
    pid=2) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_Numa_Node = DEVPROPKEY.create(
    Data1=0x540b947e,
    Data2=0x8b40,
    Data3=0x45bc,
    Data4=[0xa8, 0xa2, 0x6a, 0x0b, 0x89, 0x4c, 0xbd, 0xa2],
    pid=3) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_BusReportedDeviceDesc = DEVPROPKEY.create(
    Data1=0x540b947e,
    Data2=0x8b40,
    Data3=0x45bc,
    Data4=[0xa8, 0xa2, 0x6a, 0x0b, 0x89, 0x4c, 0xbd, 0xa2],
    pid=4) # DEVPROP_TYPE_STRING

DEVPKEY_Device_SessionId = DEVPROPKEY.create(
    Data1=0x83da6326,
    Data2=0x97a6,
    Data3=0x4088,
    Data4=[0x94, 0x53, 0xa1, 0x92, 0x3f, 0x57, 0x3b, 0x29],
    pid=6) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_InstallDate = DEVPROPKEY.create(
    Data1=0x83da6326,
    Data2=0x97a6,
    Data3=0x4088,
    Data4=[0x94, 0x53, 0xa1, 0x92, 0x3f, 0x57, 0x3b, 0x29],
    pid=100) # DEVPROP_TYPE_FILETIME

DEVPKEY_Device_FirstInstallDate = DEVPROPKEY.create(
    Data1=0x83da6326,
    Data2=0x97a6,
    Data3=0x4088,
    Data4=[0x94, 0x53, 0xa1, 0x92, 0x3f, 0x57, 0x3b, 0x29],
    pid=101) # DEVPROP_TYPE_FILETIME

DEVPKEY_Device_DriverDate = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=2) # DEVPROP_TYPE_FILETIME

DEVPKEY_Device_DriverVersion = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=3) # DEVPROP_TYPE_STRING

DEVPKEY_Device_DriverDesc = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=4) # DEVPROP_TYPE_STRING

DEVPKEY_Device_DriverInfPath = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=5) # DEVPROP_TYPE_STRING

DEVPKEY_Device_DriverInfSection = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=6) # DEVPROP_TYPE_STRING

DEVPKEY_Device_DriverInfSectionExt = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=7) # DEVPROP_TYPE_STRING

DEVPKEY_Device_MatchingDeviceId = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=8) # DEVPROP_TYPE_STRING

DEVPKEY_Device_DriverProvider = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=9) # DEVPROP_TYPE_STRING

DEVPKEY_Device_DriverPropPageProvider = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=10) # DEVPROP_TYPE_STRING

DEVPKEY_Device_DriverCoInstallers = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=11) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_Device_ResourcePickerTags = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=12) # DEVPROP_TYPE_STRING

DEVPKEY_Device_ResourcePickerExceptions = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=13) # DEVPROP_TYPE_STRING

DEVPKEY_Device_DriverRank = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=14) # DEVPROP_TYPE_UINT32

DEVPKEY_Device_DriverLogoLevel = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=15) # DEVPROP_TYPE_UINT32


DEVPKEY_Device_NoConnectSound = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=17) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_Device_GenericDriverInstalled = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=18) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_Device_AdditionalSoftwareRequested = DEVPROPKEY.create(
    Data1=0xa8b865dd,
    Data2=0x2e3d,
    Data3=0x4094,
    Data4=[0xad, 0x97, 0xe5, 0x93, 0xa7, 0xc, 0x75, 0xd6],
    pid=19) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_Device_SafeRemovalRequired = DEVPROPKEY.create(
    Data1=0xafd97640,
    Data2=0x86a3,
    Data3=0x4210,
    Data4=[0xb6, 0x7c, 0x28, 0x9c, 0x41, 0xaa, 0xbe, 0x55],
    pid=2) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_Device_SafeRemovalRequiredOverride = DEVPROPKEY.create(
    Data1=0xafd97640,
    Data2=0x86a3,
    Data3=0x4210,
    Data4=[0xb6, 0x7c, 0x28, 0x9c, 0x41, 0xaa, 0xbe, 0x55],
    pid=3) # DEVPROP_TYPE_BOOLEAN


DEVPKEY_DrvPkg_Model = DEVPROPKEY.create(
    Data1=0xcf73bb51,
    Data2=0x3abf,
    Data3=0x44a2,
    Data4=[0x85, 0xe0, 0x9a, 0x3d, 0xc7, 0xa1, 0x21, 0x32],
    pid=2) # DEVPROP_TYPE_STRING

DEVPKEY_DrvPkg_VendorWebSite = DEVPROPKEY.create(
    Data1=0xcf73bb51,
    Data2=0x3abf,
    Data3=0x44a2,
    Data4=[0x85, 0xe0, 0x9a, 0x3d, 0xc7, 0xa1, 0x21, 0x32],
    pid=3) # DEVPROP_TYPE_STRING

DEVPKEY_DrvPkg_DetailedDescription = DEVPROPKEY.create(
    Data1=0xcf73bb51,
    Data2=0x3abf,
    Data3=0x44a2,
    Data4=[0x85, 0xe0, 0x9a, 0x3d, 0xc7, 0xa1, 0x21, 0x32],
    pid=4) # DEVPROP_TYPE_STRING

DEVPKEY_DrvPkg_DocumentationLink = DEVPROPKEY.create(
    Data1=0xcf73bb51,
    Data2=0x3abf,
    Data3=0x44a2,
    Data4=[0x85, 0xe0, 0x9a, 0x3d, 0xc7, 0xa1, 0x21, 0x32],
    pid=5) # DEVPROP_TYPE_STRING

DEVPKEY_DrvPkg_Icon = DEVPROPKEY.create(
    Data1=0xcf73bb51,
    Data2=0x3abf,
    Data3=0x44a2,
    Data4=[0x85, 0xe0, 0x9a, 0x3d, 0xc7, 0xa1, 0x21, 0x32],
    pid=6) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_DrvPkg_BrandingIcon = DEVPROPKEY.create(
    Data1=0xcf73bb51,
    Data2=0x3abf,
    Data3=0x44a2,
    Data4=[0x85, 0xe0, 0x9a, 0x3d, 0xc7, 0xa1, 0x21, 0x32],
    pid=7) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_DeviceClass_UpperFilters = DEVPROPKEY.create(
    Data1=0x4321918b,
    Data2=0xf69e,
    Data3=0x470d,
    Data4=[0xa5, 0xde, 0x4d, 0x88, 0xc7, 0x5a, 0xd2, 0x4b],
    pid=19) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_DeviceClass_LowerFilters = DEVPROPKEY.create(
    Data1=0x4321918b,
    Data2=0xf69e,
    Data3=0x470d,
    Data4=[0xa5, 0xde, 0x4d, 0x88, 0xc7, 0x5a, 0xd2, 0x4b],
    pid=20) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_DeviceClass_Security = DEVPROPKEY.create(
    Data1=0x4321918b,
    Data2=0xf69e,
    Data3=0x470d,
    Data4=[0xa5, 0xde, 0x4d, 0x88, 0xc7, 0x5a, 0xd2, 0x4b],
    pid=25) # DEVPROP_TYPE_SECURITY_DESCRIPTOR

DEVPKEY_DeviceClass_SecuritySDS = DEVPROPKEY.create(
    Data1=0x4321918b,
    Data2=0xf69e,
    Data3=0x470d,
    Data4=[0xa5, 0xde, 0x4d, 0x88, 0xc7, 0x5a, 0xd2, 0x4b],
    pid=26) # DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING

DEVPKEY_DeviceClass_DevType = DEVPROPKEY.create(
    Data1=0x4321918b,
    Data2=0xf69e,
    Data3=0x470d,
    Data4=[0xa5, 0xde, 0x4d, 0x88, 0xc7, 0x5a, 0xd2, 0x4b],
    pid=27) # DEVPROP_TYPE_UINT32

DEVPKEY_DeviceClass_Exclusive = DEVPROPKEY.create(
    Data1=0x4321918b,
    Data2=0xf69e,
    Data3=0x470d,
    Data4=[0xa5, 0xde, 0x4d, 0x88, 0xc7, 0x5a, 0xd2, 0x4b],
    pid=28) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceClass_Characteristics = DEVPROPKEY.create(
    Data1=0x4321918b,
    Data2=0xf69e,
    Data3=0x470d,
    Data4=[0xa5, 0xde, 0x4d, 0x88, 0xc7, 0x5a, 0xd2, 0x4b],
    pid=29) # DEVPROP_TYPE_UINT32

DEVPKEY_DeviceClass_Name = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=2) # DEVPROP_TYPE_STRING

DEVPKEY_DeviceClass_ClassName = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=3) # DEVPROP_TYPE_STRING

DEVPKEY_DeviceClass_Icon = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=4) # DEVPROP_TYPE_STRING

DEVPKEY_DeviceClass_ClassInstaller = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=5) # DEVPROP_TYPE_STRING

DEVPKEY_DeviceClass_PropPageProvider = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=6) # DEVPROP_TYPE_STRING

DEVPKEY_DeviceClass_NoInstallClass = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=7) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceClass_NoDisplayClass = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=8) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceClass_SilentInstall = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=9) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceClass_NoUseClass = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=10) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceClass_DefaultService = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=11) # DEVPROP_TYPE_STRING

DEVPKEY_DeviceClass_IconPath = DEVPROPKEY.create(
    Data1=0x259abffc,
    Data2=0x50a7,
    Data3=0x47ce,
    Data4=[0xaf, 0x8, 0x68, 0xc9, 0xa7, 0xd7, 0x33, 0x66],
    pid=12) # DEVPROP_TYPE_STRING_LIST


DEVPKEY_DeviceClass_DHPRebalanceOptOut = DEVPROPKEY.create(
    Data1=0xd14d3ef3,
    Data2=0x66cf,
    Data3=0x4ba2,
    Data4=[0x9d, 0x38, 0x0d, 0xdb, 0x37, 0xab, 0x47, 0x01],
    pid=2) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceClass_ClassCoInstallers = DEVPROPKEY.create(
    Data1=0x713d1703,
    Data2=0xa2e2,
    Data3=0x49f5,
    Data4=[0x92, 0x14, 0x56, 0x47, 0x2e, 0xf3, 0xda, 0x5c],
    pid=2) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_DeviceInterface_FriendlyName = DEVPROPKEY.create(
    Data1=0x026e516e,
    Data2=0xb814,
    Data3=0x414b,
    Data4=[0x83, 0xcd, 0x85, 0x6d, 0x6f, 0xef, 0x48, 0x22],
    pid=2) # DEVPROP_TYPE_STRING

DEVPKEY_DeviceInterface_Enabled = DEVPROPKEY.create(
    Data1=0x026e516e,
    Data2=0xb814,
    Data3=0x414b,
    Data4=[0x83, 0xcd, 0x85, 0x6d, 0x6f, 0xef, 0x48, 0x22],
    pid=3) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceInterface_ClassGuid = DEVPROPKEY.create(
    Data1=0x026e516e,
    Data2=0xb814,
    Data3=0x414b,
    Data4=[0x83, 0xcd, 0x85, 0x6d, 0x6f, 0xef, 0x48, 0x22],
    pid=4) # DEVPROP_TYPE_GUID

DEVPKEY_DeviceInterfaceClass_DefaultInterface = DEVPROPKEY.create(
    Data1=0x14c83a99,
    Data2=0x0b3f,
    Data3=0x44b7,
    Data4=[0xbe, 0x4c, 0xa1, 0x78, 0xd3, 0x99, 0x05, 0x64],
    pid=2) # DEVPROP_TYPE_STRING

DEVPKEY_DeviceDisplay_IsShowInDisconnectedState = DEVPROPKEY.create(
    Data1=0x78c34fc8,
    Data2=0x104a,
    Data3=0x4aca,
    Data4=[0x9e, 0xa4, 0x52, 0x4d, 0x52, 0x99, 0x6e, 0x57],
    pid=0x44) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceDisplay_IsNotInterestingForDisplay = DEVPROPKEY.create(
    Data1=0x78c34fc8,
    Data2=0x104a,
    Data3=0x4aca,
    Data4=[0x9e, 0xa4, 0x52, 0x4d, 0x52, 0x99, 0x6e, 0x57],
    pid=0x4a) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceDisplay_Category = DEVPROPKEY.create(
    Data1=0x78c34fc8,
    Data2=0x104a,
    Data3=0x4aca,
    Data4=[0x9e, 0xa4, 0x52, 0x4d, 0x52, 0x99, 0x6e, 0x57],
    pid=0x5a) # DEVPROP_TYPE_STRING_LIST

DEVPKEY_DeviceDisplay_UnpairUninstall = DEVPROPKEY.create(
    Data1=0x78c34fc8,
    Data2=0x104a,
    Data3=0x4aca,
    Data4=[0x9e, 0xa4, 0x52, 0x4d, 0x52, 0x99, 0x6e, 0x57],
    pid=0x62) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceDisplay_RequiresUninstallElevation = DEVPROPKEY.create(
    Data1=0x78c34fc8,
    Data2=0x104a,
    Data3=0x4aca,
    Data4=[0x9e, 0xa4, 0x52, 0x4d, 0x52, 0x99, 0x6e, 0x57],
    pid=0x63) # DEVPROP_TYPE_BOOLEAN

DEVPKEY_DeviceDisplay_AlwaysShowDeviceAsConnected = DEVPROPKEY.create(
    Data1=0x78c34fc8,
    Data2=0x104a,
    Data3=0x4aca,
    Data4=[0x9e, 0xa4, 0x52, 0x4d, 0x52, 0x99, 0x6e, 0x57],
    pid=0x65) # DEVPROP_TYPE_BOOLEAN

DEVPROP_TYPEMOD_ARRAY = 0x00001000 # array of fixed - sized data elements
DEVPROP_TYPEMOD_LIST = 0x00002000 # list of variable - sized data elements

DEVPROP_TYPE_EMPTY = 0x00000000 # nothing, no property data
DEVPROP_TYPE_NULL = 0x00000001 # null property data
DEVPROP_TYPE_SBYTE = 0x00000002 # 8 - bit signed int (SBYTE)
DEVPROP_TYPE_BYTE = 0x00000003 # 8 - bit unsigned int (BYTE)
DEVPROP_TYPE_INT16 = 0x00000004  # 16-bit signed int (SHORT)
DEVPROP_TYPE_UINT16 = 0x00000005  # 16-bit unsigned int (USHORT)
DEVPROP_TYPE_INT32 = 0x00000006  # 32-bit signed int (LONG)
DEVPROP_TYPE_UINT32 = 0x00000007  # 32-bit unsigned int (ULONG)
DEVPROP_TYPE_INT64 = 0x00000008  # 64-bit signed int (LONG64)
DEVPROP_TYPE_UINT64 = 0x00000009  # 64-bit unsigned int (ULONG64)
DEVPROP_TYPE_FLOAT = 0x0000000A # 32 - bit floating - point (FLOAT)
DEVPROP_TYPE_DOUBLE = 0x0000000B # 64 - bit floating - point (DOUBLE)
DEVPROP_TYPE_DECIMAL = 0x0000000C # 128 - bit data (DECIMAL)
DEVPROP_TYPE_GUID = 0x0000000D # 128 - bit unique identifier (GUID)
DEVPROP_TYPE_CURRENCY = 0x0000000E # 64 bit signed int currency value (CURRENCY)
DEVPROP_TYPE_DATE = 0x0000000F # date (DATE)
DEVPROP_TYPE_FILETIME = 0x00000010 # file time (FILETIME)
DEVPROP_TYPE_BOOLEAN = 0x00000011 # 8 - bit boolean (DEVPROP_BOOLEAN)
DEVPROP_TYPE_STRING = 0x00000012 # null - terminated string
DEVPROP_TYPE_STRING_LIST = DEVPROP_TYPE_STRING | DEVPROP_TYPEMOD_LIST # multi-sz string list
DEVPROP_TYPE_SECURITY_DESCRIPTOR = 0x00000013 # self - relative binary SECURITY_DESCRIPTOR
DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING = 0x00000014 # security descriptor string (SDDL format)
DEVPROP_TYPE_DEVPROPKEY = 0x00000015 # device property key (DEVPROPKEY)
DEVPROP_TYPE_DEVPROPTYPE = 0x00000016 # device property type (DEVPROPTYPE)
DEVPROP_TYPE_BINARY = DEVPROP_TYPE_BYTE | DEVPROP_TYPEMOD_ARRAY   # custom binary data
DEVPROP_TYPE_ERROR = 0x00000017 # 32 - bit Win32 system error code
DEVPROP_TYPE_NTSTATUS = 0x00000018 # 32 - bit NTSTATUS code
DEVPROP_TYPE_STRING_INDIRECT = 0x00000019 # string resource (@[path\] < dllname > , -<strId >)

MAX_DEVPROP_TYPE = 0x00000019 # max valid DEVPROP_TYPE_ value
MAX_DEVPROP_TYPEMOD = 0x00002000 # max valid DEVPROP_TYPEMOD_ value

DEVPROP_MASK_TYPE = 0x00000FFF # range for base DEVPROP_TYPE_ values
DEVPROP_MASK_TYPEMOD = 0x0000F000 # mask for DEVPROP_TYPEMOD_ type modifiers

# 8 - bit boolean type definition for DEVPROP_TYPE_BOOLEAN (True= -1, False=0)
CHAR = BYTE
DEVPROP_BOOLEAN = CHAR
