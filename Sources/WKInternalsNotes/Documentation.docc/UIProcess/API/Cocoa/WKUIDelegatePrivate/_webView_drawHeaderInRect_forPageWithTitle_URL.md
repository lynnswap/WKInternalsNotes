# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:drawHeaderInRect:forPageWithTitle:URL:)``

印刷時のヘッダー描画を delegate に依頼する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView drawHeaderInRect:(CGRect)rect forPageWithTitle:(NSString *)title URL:(NSURL *)url WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIClient が rect / title / URL を渡して描画を委譲する。

## References
- [`WKUIDelegatePrivate.h#L325`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L325)
- [`UIDelegate.mm#L1018`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1018)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
