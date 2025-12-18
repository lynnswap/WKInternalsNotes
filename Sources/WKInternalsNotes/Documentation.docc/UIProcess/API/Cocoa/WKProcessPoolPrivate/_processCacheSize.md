# ``WKInternalsNotes/WKProcessPool/_processCacheSize()``

WebProcessCache の現在サイズを返す。

## Objective-C Declaration
```objective-c
- (NSUInteger)_processCacheSize WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`_processPool->webProcessCache().size()` を返す。

## References
- [`WKProcessPoolPrivate.h#L148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L148)
- [`WKProcessPool.mm#L513`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L513)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
