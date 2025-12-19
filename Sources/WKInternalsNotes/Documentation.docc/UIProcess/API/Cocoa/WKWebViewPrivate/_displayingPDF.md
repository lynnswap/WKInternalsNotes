# ``WKInternalsNotes/WKWebView/_displayingPDF``

`_displayingPDF` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isDisplayingPDF) BOOL _displayingPDF WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
読み取り専用のため setter は持たない。 getter は `_isDisplayingPDF`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L395`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L395)
- [`API/Cocoa/WKWebView.mm#L5865`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5865)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
