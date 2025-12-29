# ``WKInternalsNotes/_WKInspectorDebuggableInfo/debuggableType``

デバッグ対象の種別を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) _WKInspectorDebuggableType debuggableType;
```

## Default Value
`DebuggableInfoData` の初期値に依存する。

## Discussion
`API::DebuggableInfo` の `debuggableType` をブリッジして読み書きする。getter は `toWKInspectorDebuggableType` で変換し、setter は `fromWKInspectorDebuggableType` に変換して保存する。

## References
- [`_WKInspectorDebuggableInfo.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDebuggableInfo.h#L45)
- [`_WKInspectorDebuggableInfo.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDebuggableInfo.mm#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
