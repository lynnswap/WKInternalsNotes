# ``WKInternalsNotes/_WKPageLoadTiming/navigationStart``

ナビゲーション開始時刻を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSDate *navigationStart;
```

## Default Value
`timing.navigationStart()` を `NSDate` 変換した値（未設定なら `nil`）。

## Discussion
`_navigationStart` を `nsDateFromMonotonicTime` に渡して返す。

## References
- [`_WKPageLoadTiming.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.h#L34)
- [`_WKPageLoadTiming.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.mm#L61)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
