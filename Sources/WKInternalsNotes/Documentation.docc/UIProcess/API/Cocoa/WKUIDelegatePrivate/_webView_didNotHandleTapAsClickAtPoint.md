# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didNotHandleTapAsClickAtPoint:)``

タップがクリックとして扱われなかったことを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didNotHandleTapAsClickAtPoint:(CGPoint)point;
```

## Discussion
UIClient が point を渡して delegate に通知する。

## References
- [`WKUIDelegatePrivate.h#L211`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L211)
- [`UIDelegate.mm#L169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L169)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
