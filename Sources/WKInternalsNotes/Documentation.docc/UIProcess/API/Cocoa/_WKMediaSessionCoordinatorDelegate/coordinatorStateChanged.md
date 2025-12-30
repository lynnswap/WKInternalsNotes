# ``WKInternalsNotes/_WKMediaSessionCoordinatorDelegate/coordinatorStateChanged(_:)``

状態変更を `MediaSessionCoordinatorClient` に伝える。

## Objective-C Declaration
```objective-c
- (void)coordinatorStateChanged:(_WKMediaSessionCoordinatorState)state;
```

## Discussion
`WKMediaSessionCoordinatorHelper` が enum 値の一致を `static_assert` で確認した上で `coordinatorStateChanged` を呼ぶ。

## References
- [`WKWebViewPrivateForTesting.h#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L215)
- [`WKWebViewTesting.mm#L1182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L1182)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
