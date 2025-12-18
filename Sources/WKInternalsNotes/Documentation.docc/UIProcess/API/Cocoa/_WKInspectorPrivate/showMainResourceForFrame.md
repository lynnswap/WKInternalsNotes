# ``WKInternalsNotes/_WKInspector/showMainResourceForFrame(_:)``

指定フレームのメインリソースをインスペクタで表示する。

## Objective-C Declaration
```objective-c
- (void)showMainResourceForFrame:(_WKFrameHandle *)frame;
```

## Discussion
フレームハンドルと `frameID` が取得できる場合に `showMainResourceForFrame` を呼び出し、インスペクタを表示して対象フレームのメインリソースを開く。

## References
- [`_WKInspector.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L54)
- [`_WKInspector.mm#L170`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L170)
- [`WebInspectorUIProxy.cpp#L292`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L292)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
