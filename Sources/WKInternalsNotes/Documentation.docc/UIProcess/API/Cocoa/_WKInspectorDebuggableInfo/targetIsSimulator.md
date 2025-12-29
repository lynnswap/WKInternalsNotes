# ``WKInternalsNotes/_WKInspectorDebuggableInfo/targetIsSimulator``

デバッグ対象がシミュレータかどうかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL targetIsSimulator;
```

## Default Value
`DebuggableInfoData` の初期値に依存する。

## Discussion
`API::DebuggableInfo` の `targetIsSimulator` をそのまま読み書きする。

## References
- [`_WKInspectorDebuggableInfo.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDebuggableInfo.h#L49)
- [`_WKInspectorDebuggableInfo.mm#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDebuggableInfo.mm#L83)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
