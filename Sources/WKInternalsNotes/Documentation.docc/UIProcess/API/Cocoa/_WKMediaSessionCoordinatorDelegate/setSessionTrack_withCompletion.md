# ``WKInternalsNotes/_WKMediaSessionCoordinatorDelegate/setSessionTrack(_:withCompletion:)``

`MediaSessionCoordinatorClient` のトラック設定を呼ぶ。

## Objective-C Declaration
```objective-c
- (void)setSessionTrack:(NSString*)trackIdentifier withCompletion:(void(^)(BOOL))completionHandler;
```

## Discussion
`WKMediaSessionCoordinatorHelper` が `setSessionTrack` に `trackIdentifier` を渡して転送する。

## References
- [`WKWebViewPrivateForTesting.h#L214`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L214)
- [`WKWebViewTesting.mm#L1177`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L1177)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
