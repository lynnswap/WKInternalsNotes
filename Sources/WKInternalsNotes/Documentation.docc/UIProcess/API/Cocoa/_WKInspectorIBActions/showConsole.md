# ``WKInternalsNotes/_WKInspectorIBActions/showConsole()``

Console タブを表示する。

## Objective-C Declaration
```objective-c
- (void)showConsole;
```

## Discussion
`_WKInspector` 実装では内部の `WebInspectorProxy` に `showConsole()` を転送する。

## References
- [`_WKInspectorIBActions.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorIBActions.h#L47)
- [`_WKInspector.mm#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
