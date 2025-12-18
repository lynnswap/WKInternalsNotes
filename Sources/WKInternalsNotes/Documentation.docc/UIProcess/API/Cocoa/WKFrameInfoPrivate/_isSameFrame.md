# ``WKInternalsNotes/WKFrameInfo/_isSameFrame(_:)``

別の WKFrameInfo が同じフレームかどうかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_isSameFrame:(WKFrameInfo *)frame WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
両方の `_handle.frameID` を比較して一致を返す。`ALLOW_DEPRECATED_DECLARATIONS_BEGIN/END` で `frameID` の参照を囲っている。

## References
- [`WKFrameInfoPrivate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L48)
- [`WKFrameInfo.mm#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L165)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
