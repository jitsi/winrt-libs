{
  "variables": {
    "MSVC_VERSION": "14.24.28314",
    "WIN10_SDK_VERSION": "10.0.18362.0",
    "WIN_VER": "v10",
    "USE_ADDITIONAL_WINMD": "true"
  },
  "includes": ["common.gypi"],
  "targets": [{
    "target_name": "binding",
    "sources": [],
    "include_dirs": [
      "<!(node -e \"require('nan')\")"
    ],
    "libraries": [],
    "conditions": [
      ["OS=='win'", {
        "libraries": ["-lruntimeobject.lib"],
        "sources": [
          "_nodert_generated.cpp",
          "NodeRtUtils.cpp",
          "OpaqueWrapper.cpp",
          "CollectionsConverterUtils.cpp"
        ]
      }],
      ["WIN_VER==\"v8.0\"", {
          "msvs_settings": {
            "VCCLCompilerTool": {
              "AdditionalUsingDirectories": [
                "%ProgramFiles(x86)%/Microsoft SDKs/Windows/v8.0/ExtensionSDKs/Microsoft.VCLibs/11.0/References/CommonConfiguration/neutral",
                "%ProgramFiles(x86)%/Windows Kits/8.0/References/CommonConfiguration/Neutral",
                "%ProgramFiles%/Microsoft SDKs/Windows/v8.0/ExtensionSDKs/Microsoft.VCLibs/11.0/References/CommonConfiguration/neutral",
                "%ProgramFiles%/Windows Kits/8.0/References/CommonConfiguration/Neutral"
              ]
            }
          }
        }
      ],
      ["WIN_VER==\"v8.1\"", {
        "msvs_settings": {
          "VCCLCompilerTool": {
            "AdditionalUsingDirectories": [
              "%ProgramFiles(x86)%/Microsoft SDKs/Windows/v8.1/ExtensionSDKs/Microsoft.VCLibs/12.0/References/CommonConfiguration/neutral",
              "%ProgramFiles(x86)%/Windows Kits/8.1/References/CommonConfiguration/Neutral",
              "%ProgramFiles%/Microsoft SDKs/Windows/v8.1/ExtensionSDKs/Microsoft.VCLibs/12.0/References/CommonConfiguration/neutral",
              "%ProgramFiles%/Windows Kits/8.1/References/CommonConfiguration/Neutral"
            ]
          }
        }
      }],
      ["WIN_VER==\"v10\"", {
        "msvs_settings": {
          "VCCLCompilerTool": {
            "AdditionalUsingDirectories": [
              "%ProgramFiles(x86)%/Microsoft Visual Studio 14.0/VC/lib/store/references",
              "%ProgramFiles%/Microsoft Visual Studio 14.0/VC/lib/store/references",
              "%ProgramFiles(x86)%/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/<(MSVC_VERSION)/lib/x86/store/references",
              "%ProgramFiles%/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/<(MSVC_VERSION)/lib/x86/store/references"
            ]
          }
        }
      }],
      ["USE_ADDITIONAL_WINMD==\"true\"", {
        "msvs_settings": {
          "VCCLCompilerTool": {
            "AdditionalUsingDirectories": [
              "%ProgramFiles%/Windows Kits/10/UnionMetadata/<(WIN10_SDK_VERSION)",
              "%ProgramFiles%/Windows Kits/10/Include/<(WIN10_SDK_VERSION)/um",
              "%ProgramFiles(x86)%/Windows Kits/10/UnionMetadata/<(WIN10_SDK_VERSION)",
              "%ProgramFiles(x86)%/Windows Kits/10/Include/<(WIN10_SDK_VERSION)/um"
            ]
          }
        }
      }]
    ],
    "msvs_settings": {
      "VCCLCompilerTool": {
        "AdditionalOptions": ["/ZW"],
        "DisableSpecificWarnings": [4609, 4996]
      }
    }
  }]
}