# ``WKInternalsNotes/_WKMediaSessionCoordinator/readyStateChanged(_:)``

MediaSession の ready state をクライアントに伝える。

## Objective-C Declaration
```objective-c
- (void)readyStateChanged:(_WKMediaSessionReadyState)state;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` は enum の一致を `static_assert` で確認した上で `_WKMediaSessionReadyState` にキャストして渡す。

## References
- [`WKWebViewPrivateForTesting.h#L228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L228)
- [`WKWebViewTesting.mm#L888`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L888)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
