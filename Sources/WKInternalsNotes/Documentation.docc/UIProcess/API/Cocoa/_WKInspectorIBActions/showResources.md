# ``WKInternalsNotes/_WKInspectorIBActions/showResources()``

Sources タブを表示する。

## Objective-C Declaration
```objective-c
- (void)showResources;
```

## Discussion
`_WKInspector` 実装では内部の `WebInspectorProxy` に `showResources()` を転送する。

## References
- [`_WKInspectorIBActions.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorIBActions.h#L52)
- [`_WKInspector.mm#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L165)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
