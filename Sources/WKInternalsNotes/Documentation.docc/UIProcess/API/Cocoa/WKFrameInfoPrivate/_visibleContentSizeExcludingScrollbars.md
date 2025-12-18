# ``WKInternalsNotes/WKFrameInfo/_visibleContentSizeExcludingScrollbars``

スクロールバーを除いた可視コンテンツサイズを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGSize _visibleContentSizeExcludingScrollbars WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
`frameMetrics.visibleContentSizeExcludingScrollbars` の値。

## Discussion
`frameInfoData().frameMetrics.visibleContentSizeExcludingScrollbars` を `CGSize` にキャストして返す。

## References
- [`WKFrameInfoPrivate.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L45)
- [`WKFrameInfo.mm#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L155)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
