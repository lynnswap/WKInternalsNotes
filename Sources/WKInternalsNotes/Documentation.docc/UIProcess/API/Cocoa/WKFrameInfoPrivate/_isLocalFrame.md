# ``WKInternalsNotes/WKFrameInfo/_isLocalFrame``

ローカルフレームかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isLocalFrame WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
`_frameInfo->isLocalFrame()` の結果。

## Discussion
FrameType が Local かどうかの判定結果をそのまま返す。

## References
- [`WKFrameInfoPrivate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L38)
- [`WKFrameInfo.mm#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L120)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
