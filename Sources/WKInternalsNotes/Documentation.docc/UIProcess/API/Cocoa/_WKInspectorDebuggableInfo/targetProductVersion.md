# ``WKInternalsNotes/_WKInspectorDebuggableInfo/targetProductVersion``

デバッグ対象のプロダクトバージョンを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *targetProductVersion;
```

## Default Value
`DebuggableInfoData` の初期値に依存する。

## Discussion
`API::DebuggableInfo` の `targetProductVersion` を `NSString` として取得/設定する。

## References
- [`_WKInspectorDebuggableInfo.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDebuggableInfo.h#L48)
- [`_WKInspectorDebuggableInfo.mm#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDebuggableInfo.mm#L73)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
