# ``WKInternalsNotes/_WKInspectorIBActions/show()``

Web Inspector を表示する。

## Objective-C Declaration
```objective-c
- (void)show;
```

## Discussion
`_WKInspector` 実装では内部の `WebInspectorProxy` に `show()` を転送する。

## References
- [`_WKInspectorIBActions.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorIBActions.h#L36)
- [`_WKInspector.mm#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L145)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
