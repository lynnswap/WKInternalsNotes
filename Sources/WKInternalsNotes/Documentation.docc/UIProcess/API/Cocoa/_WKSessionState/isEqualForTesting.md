# ``WKInternalsNotes/_WKSessionState/isEqualForTesting(_:)``

`SessionState` のテスト用比較を行う。

## Objective-C Declaration
```objective-c
- (BOOL)isEqualForTesting:(_WKSessionState *)other WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
`_sessionState.isEqualForTesting` に委譲して比較する。

## References
- [`_WKSessionState.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSessionState.h#L34)
- [`_WKSessionState.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSessionState.mm#L61)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
