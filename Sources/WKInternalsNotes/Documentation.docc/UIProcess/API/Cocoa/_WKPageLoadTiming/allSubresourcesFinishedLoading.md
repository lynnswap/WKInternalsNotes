# ``WKInternalsNotes/_WKPageLoadTiming/allSubresourcesFinishedLoading``

全サブリソース読み込み完了時刻を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSDate *allSubresourcesFinishedLoading;
```

## Default Value
`timing.allSubresourcesFinishedLoading()` を `NSDate` 変換した値（未設定なら `nil`）。

## Discussion
`_allSubresourcesFinishedLoading` を `nsDateFromMonotonicTime` に渡して返す。

## References
- [`_WKPageLoadTiming.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.h#L38)
- [`_WKPageLoadTiming.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.mm#L81)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
