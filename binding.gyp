{
  "targets": [
    {
      "target_name": "directfb",
      "sources": [ 
          "src/directfb.cc",
          "src/common.cc",
          "src/templates.cc",
          "src/directfb_v8.cc",
          "src/IDirectFB.cc" ,
          "src/IDirectFBDataBuffer.cc",
          "src/IDirectFBDisplayLayer.cc",
          "src/IDirectFBEventBuffer.cc",
          "src/IDirectFBFont.cc",
          "src/IDirectFBGL.cc",
          "src/IDirectFBImageProvider.cc",
          "src/IDirectFBInputDevice.cc",
          "src/IDirectFBPalette.cc",
          "src/IDirectFBScreen.cc",
          "src/IDirectFBSurface.cc",
          "src/IDirectFBVideoProvider.cc",
          "src/IDirectFBWindow.cc"
      ],
      "include_dirs" : [ "/usr/include/directfb/" ],
      "libraries": [ "-Llibdirectfb.a" ]
    }
  ]
  
}