# ``WKInternalsNotes/_WKPageLoadTiming/firstMeaningfulPaint``

最初の意味的ペイント時刻を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSDate *firstMeaningfulPaint;
```

## Default Value
`timing.firstMeaningfulPaint()` を `NSDate` 変換した値（未設定なら `nil`）。

## Discussion
`_firstMeaningfulPaint` を `nsDateFromMonotonicTime` に渡して返す。

## References
- [`_WKPageLoadTiming.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.h#L36)
- [`_WKPageLoadTiming.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.mm#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
