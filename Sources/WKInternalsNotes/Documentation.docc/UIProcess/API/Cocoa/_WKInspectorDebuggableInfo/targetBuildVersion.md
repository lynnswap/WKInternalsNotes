# ``WKInternalsNotes/_WKInspectorDebuggableInfo/targetBuildVersion``

デバッグ対象のビルドバージョンを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *targetBuildVersion;
```

## Default Value
`DebuggableInfoData` の初期値に依存する。

## Discussion
`API::DebuggableInfo` の `targetBuildVersion` を `NSString` として取得/設定する。

## References
- [`_WKInspectorDebuggableInfo.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDebuggableInfo.h#L47)
- [`_WKInspectorDebuggableInfo.mm#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDebuggableInfo.mm#L63)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
