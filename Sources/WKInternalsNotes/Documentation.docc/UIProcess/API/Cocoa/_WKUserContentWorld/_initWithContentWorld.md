# ``WKInternalsNotes/_WKUserContentWorld/_initWithContentWorld(_:)``

既存の `WKContentWorld` を保持して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithContentWorld:(WKContentWorld *)world;
```

## Discussion
`world` を `_contentWorld` に保持して返す。

## References
- [`_WKUserContentWorldInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentWorldInternal.h#L37)
- [`_WKUserContentWorld.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentWorld.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
