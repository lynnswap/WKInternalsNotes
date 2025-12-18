# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didNotHandleTapAsClickAtPoint:)``

タップがクリックとして扱われなかったことを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didNotHandleTapAsClickAtPoint:(CGPoint)point;
```

## Discussion
UIClient が point を渡して delegate に通知する。

## References
- [`WKUIDelegatePrivate.h#L234`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L234)
- [`UIDelegate.mm#L1665`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1665)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
