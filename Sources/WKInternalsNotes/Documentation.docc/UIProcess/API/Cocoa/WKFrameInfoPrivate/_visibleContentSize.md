# ``WKInternalsNotes/WKFrameInfo/_visibleContentSize``

可視コンテンツサイズを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGSize _visibleContentSize WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
`frameMetrics.visibleContentSize` の値。

## Discussion
`frameInfoData().frameMetrics.visibleContentSize` を `CGSize` にキャストして返す。

## References
- [`WKFrameInfoPrivate.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L44)
- [`WKFrameInfo.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L150)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
