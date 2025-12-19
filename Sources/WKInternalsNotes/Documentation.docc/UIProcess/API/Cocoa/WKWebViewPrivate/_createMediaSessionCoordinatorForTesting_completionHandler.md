# ``WKInternalsNotes/WKWebView/_createMediaSessionCoordinatorForTesting(_:completionHandler:)``

`_createMediaSessionCoordinatorForTesting` を実行する。

## Objective-C Declaration
```objective-c
- (void)_createMediaSessionCoordinatorForTesting:(id <_WKMediaSessionCoordinator>)privateCoordinator completionHandler:(void(^)(BOOL))completionHandler;
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivateForTesting.h#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L140)
- [`WKWebViewTesting.mm#L732`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L732)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
