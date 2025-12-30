# ``WKInternalsNotes/_WKMediaSessionCoordinatorDelegate/playSessionWithCompletion(_:)``

`MediaSessionCoordinatorClient` の `playSession` を呼ぶ。

## Objective-C Declaration
```objective-c
- (void)playSessionWithCompletion:(void(^)(BOOL))completionHandler;
```

## Discussion
`WKMediaSessionCoordinatorHelper` が `playSession` を `atTime`/`hostTime` 未指定で呼び出す。

## References
- [`WKWebViewPrivateForTesting.h#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L212)
- [`WKWebViewTesting.mm#L1167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L1167)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
