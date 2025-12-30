# ``WKInternalsNotes/_WKSessionState/_initWithSessionState(_:)``

`SessionState` を受け取って初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithSessionState:(WebKit::SessionState)sessionState;
```

## Discussion
`_sessionState` に `WTFMove` で代入して返す。

## References
- [`_WKSessionStateInternal.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSessionStateInternal.h#L35)
- [`_WKSessionState.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSessionState.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
