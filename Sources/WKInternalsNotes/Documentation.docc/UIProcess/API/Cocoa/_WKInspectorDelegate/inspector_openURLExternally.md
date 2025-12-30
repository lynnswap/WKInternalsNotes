# ``WKInternalsNotes/_WKInspectorDelegate/inspector(_:openURLExternally:)``

外部で URL を開く要求を受ける。

## Objective-C Declaration
```objective-c
- (void)inspector:(_WKInspector *)inspector openURLExternally:(NSURL *)url;
```

## Discussion
`InspectorClient::openURLExternally` から delegate が応答可能な場合に呼ばれ、`NSURL` に変換した URL を渡す。

## References
- [`_WKInspectorDelegate.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorDelegate.h#L39)
- [`_WKInspector.mm#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L65)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
