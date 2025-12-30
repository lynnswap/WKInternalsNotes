# ``WKInternalsNotes/_WKPageLoadTiming/firstVisualLayout``

最初のビジュアルレイアウト時刻を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSDate *firstVisualLayout;
```

## Default Value
`timing.firstVisualLayout()` を `NSDate` 変換した値（未設定なら `nil`）。

## Discussion
`_firstVisualLayout` を `nsDateFromMonotonicTime` に渡して返す。

## References
- [`_WKPageLoadTiming.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.h#L35)
- [`_WKPageLoadTiming.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
