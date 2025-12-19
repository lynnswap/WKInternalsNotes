# ``WKInternalsNotes/WKWebView/_createWebArchiveForFrames(_:rootFrame:completionHandler:)``

`_createWebArchiveForFrames` を実行する。

## Objective-C Declaration
```objective-c
- (void)_createWebArchiveForFrames:(NSArray<WKFrameInfo *> *)frames rootFrame:(WKFrameInfo *)rootFrame completionHandler:(void (^)(NSData *, NSError *))completionHandler WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L363`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L363)
- [`API/Cocoa/WKWebView.mm#L5416`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5416)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
