# ``WKInternalsNotes/WKWebView/_requestTargetedElementInfo(_:completionHandler:)``

`_requestTargetedElementInfo` を取得する。

## Objective-C Declaration
```objective-c
- (void)_requestTargetedElementInfo:(_WKTargetedElementRequest *)request completionHandler:(void(^)(NSArray<_WKTargetedElementInfo *> *))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L613`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L613)
- [`WKWebView.mm#L4564`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4564)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
