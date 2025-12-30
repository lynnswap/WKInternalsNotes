# ``WKInternalsNotes/_WKMediaSessionCoordinator/trackIdentifierChanged(_:)``

トラック識別子の変更をクライアントに伝える。

## Objective-C Declaration
```objective-c
- (void)trackIdentifierChanged:(NSString *)trackIdentifier;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` は `String` を `NSString` に変換して `trackIdentifierChanged:` を呼ぶ。

## References
- [`WKWebViewPrivateForTesting.h#L230`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L230)
- [`WKWebViewTesting.mm#L908`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L908)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
