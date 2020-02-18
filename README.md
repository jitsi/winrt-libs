WinRT native APIs wrapped with NodeRT
=====

These native windows APIs are used in some Jitsi products to gain native functionalities, such as Bluetooth Beacon support.

# APIs

- windows.devices.bluetooth.advertisement: <https://docs.microsoft.com/en-us/uwp/api/windows.devices.bluetooth.advertisement>
- windows.storage.streams: <https://docs.microsoft.com/en-us/uwp/api/windows.storage.streams>

# Dependencies

Both libraries require Win 10 SDK ver 10.0.18362.0 and Visual Studio 2019 ver 14.24.28314 to be installed for compiling on Windows 10. If other versions are preferred see the `VARIABLES` section in the `binding.gyp` file. These variables can also be set from the command line in build time, see gyp documentation for more info.
