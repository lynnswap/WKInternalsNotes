# ``WKInternalsNotes/_WKMediaSessionCoordinatorDelegate/seekSessionToTime(_:withCompletion:)``

`MediaSessionCoordinatorClient` に seek を転送する。

## Objective-C Declaration
```objective-c
- (void)seekSessionToTime:(double)time withCompletion:(void(^)(BOOL))completionHandler;
```

## Discussion
`WKMediaSessionCoordinatorHelper` が `seekSessionToTime` を呼び、`completionHandler` を `makeBlockPtr` で渡す。

## References
- [`WKWebViewPrivateForTesting.h#L211`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L211)
- [`WKWebViewTesting.mm#L1162`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L1162)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
