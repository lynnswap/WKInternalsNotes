# ``WKInternalsNotes/WKWebView/_attachmentForIdentifier(_:)``

`_attachmentForIdentifier` を実行する。

## Objective-C Declaration
```objective-c
- (_WKAttachment *)_attachmentForIdentifier:(NSString *)identifier WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L303`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L303)
- [`API/Cocoa/WKWebView.mm#L5057`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5057)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
