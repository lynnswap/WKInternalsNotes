# ``WKInternalsNotes/_WKInspectorIBActions/close()``

Web Inspector を閉じる。

## Objective-C Declaration
```objective-c
- (void)close;
```

## Discussion
`_WKInspector` 実装では内部の `WebInspectorProxy` に `close()` を転送する。

## References
- [`_WKInspectorIBActions.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorIBActions.h#L42)
- [`_WKInspector.mm#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L155)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
