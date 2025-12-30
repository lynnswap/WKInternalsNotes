# ``WKInternalsNotes/_WKMediaSessionCoordinatorDelegate/pauseSessionWithCompletion(_:)``

`MediaSessionCoordinatorClient` の `pauseSession` を呼ぶ。

## Objective-C Declaration
```objective-c
- (void)pauseSessionWithCompletion:(void(^)(BOOL))completionHandler;
```

## Discussion
`WKMediaSessionCoordinatorHelper` が `pauseSession` に `completionHandler` を転送する。

## References
- [`WKWebViewPrivateForTesting.h#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L213)
- [`WKWebViewTesting.mm#L1172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L1172)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
