# ``WKInternalsNotes/WKProcessPool/_setPLTResourceDelayIntervalForTesting(_:)``

PLT リソース遅延間隔を設定する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_setPLTResourceDelayIntervalForTesting:(NSTimeInterval)interval;
```

## Discussion
`_processPool->setPLTResourceDelayInterval(Seconds(interval))` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L126)
- [`WKProcessPool.mm#L557`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L557)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
