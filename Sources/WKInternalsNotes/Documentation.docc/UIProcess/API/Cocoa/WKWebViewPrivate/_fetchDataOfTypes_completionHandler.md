# ``WKInternalsNotes/WKWebView/_fetchDataOfTypes(_:completionHandler:)``

`_fetchDataOfTypes` を取得する。

## Objective-C Declaration
```objective-c
- (void)_fetchDataOfTypes:(_WKWebViewDataType)dataTypes completionHandler:(WK_SWIFT_UI_ACTOR void (^)(NSData *))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L635`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L635)
- [`WKWebView.mm#L6425`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6425)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
