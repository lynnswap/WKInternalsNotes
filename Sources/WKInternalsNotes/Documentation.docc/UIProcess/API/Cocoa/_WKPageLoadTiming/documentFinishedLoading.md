# ``WKInternalsNotes/_WKPageLoadTiming/documentFinishedLoading``

ドキュメント読み込み完了時刻を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSDate *documentFinishedLoading;
```

## Default Value
`timing.documentFinishedLoading()` を `NSDate` 変換した値（未設定なら `nil`）。

## Discussion
`_documentFinishedLoading` を `nsDateFromMonotonicTime` に渡して返す。

## References
- [`_WKPageLoadTiming.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.h#L37)
- [`_WKPageLoadTiming.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPageLoadTiming.mm#L76)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
