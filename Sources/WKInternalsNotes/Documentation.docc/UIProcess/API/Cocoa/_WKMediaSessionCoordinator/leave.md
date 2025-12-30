# ``WKInternalsNotes/_WKMediaSessionCoordinator/leave()``

テスト用 coordinator では `leave` をクライアントに転送する。

## Objective-C Declaration
```objective-c
- (void)leave;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` が `m_clientCoordinator` の `leave` を呼ぶ。

## References
- [`WKWebViewPrivateForTesting.h#L222`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L222)
- [`WKWebViewTesting.mm#L820`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L820)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
