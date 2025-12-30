# ``WKInternalsNotes/_WKPageLoadTiming/_initWithTiming(_:)``

`WebPageLoadTiming` を保持して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithTiming:(const WebKit::WebPageLoadTiming&)timing;
```

## Discussion
`timing` から各 `WallTime` を取得して内部に保持する。

## References
- [`_WKPageLoadTimingInternal.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTimingInternal.h#L36)
- [`_WKPageLoadTiming.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.mm#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
