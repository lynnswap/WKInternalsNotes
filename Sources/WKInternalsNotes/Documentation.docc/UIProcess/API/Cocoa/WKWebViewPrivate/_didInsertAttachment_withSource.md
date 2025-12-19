# ``WKInternalsNotes/WKWebView/_didInsertAttachment(_:withSource:)``

`_didInsertAttachment` を実行する。

## Objective-C Declaration
```objective-c
- (void)_didInsertAttachment:(API::Attachment&)attachment withSource:(NSString *)source;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewInternal.h#L520`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L520)
- [`API/Cocoa/WKWebView.mm#L2094`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2094)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
