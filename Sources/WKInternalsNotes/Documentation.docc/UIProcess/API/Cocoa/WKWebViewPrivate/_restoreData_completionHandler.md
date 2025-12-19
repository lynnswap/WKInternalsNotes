# ``WKInternalsNotes/WKWebView/_restoreData(_:completionHandler:)``

`_restoreData` を実行する。

## Objective-C Declaration
```objective-c
- (void)_restoreData:(NSData *)data completionHandler:(WK_SWIFT_UI_ACTOR void(^)(BOOL))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L636`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L636)
- [`WKWebView.mm#L6433`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6433)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
