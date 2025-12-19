# ``WKInternalsNotes/WKWebView/_takeSnapshotOfNode(_:completionHandler:)``

`_takeSnapshotOfNode` を実行する。

## Objective-C Declaration
```objective-c
- (void)_takeSnapshotOfNode:(_WKJSHandle *)node completionHandler:(WK_SWIFT_UI_ACTOR void (^)(UIImage *, NSError *))completionHandler WK_SWIFT_ASYNC_NAME(_takeSnapshotOfNode(_:)) WK_API_AVAILABLE(ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L650`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L650)
- [`WKWebView.mm#L6485`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6485)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
