# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didAdjustVisibilityWithSelectors:)``

可視性を調整した selector 群を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didAdjustVisibilityWithSelectors:(NSArray<NSString *> *)selectors WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
UIClient が selector の配列を `NSArray` に変換して delegate に渡す。

## References
- [`WKUIDelegatePrivate.h#L196`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L196)
- [`UIDelegate.mm#L231`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L231)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
