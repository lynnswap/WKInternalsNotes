# ``WKInternalsNotes/WKFrameInfo/_errorOccurred``

フレームでエラーが発生したかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _errorOccurred WK_API_AVAILABLE(macos(14.4), ios(17.4), visionos(1.1));
```

## Default Value
`_frameInfo->errorOccurred()` の結果。

## Discussion
FrameInfoData の `errorOccurred` を参照する。

## References
- [`WKFrameInfoPrivate.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L40)
- [`WKFrameInfo.mm#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L130)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
