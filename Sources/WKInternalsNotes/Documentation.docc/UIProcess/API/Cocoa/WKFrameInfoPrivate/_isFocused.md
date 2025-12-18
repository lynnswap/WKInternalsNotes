# ``WKInternalsNotes/WKFrameInfo/_isFocused``

フレームがフォーカス中かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isFocused WK_API_AVAILABLE(macos(14.4), ios(17.4), visionos(1.1));
```

## Default Value
`_frameInfo->isFocused()` の結果。

## Discussion
FrameInfoData の `isFocused` を参照する。

## References
- [`WKFrameInfoPrivate.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L39)
- [`WKFrameInfo.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L125)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
