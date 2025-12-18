# ``WKInternalsNotes/WKFrameInfo/_contentSize``

フレームのコンテンツサイズを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGSize _contentSize WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
`frameMetrics.contentSize` の値。

## Discussion
`frameInfoData().frameMetrics.contentSize` を `CGSize` にキャストして返す。

## References
- [`WKFrameInfoPrivate.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L43)
- [`WKFrameInfo.mm#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L145)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
