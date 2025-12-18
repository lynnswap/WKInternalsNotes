# ``WKInternalsNotes/WKFrameInfo/_processIdentifier``

フレームのプロセス ID を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) pid_t _processIdentifier WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
`_frameInfo->processID()` の値。

## Discussion
API::FrameInfo が保持する `ProcessID` を `pid_t` として返す。

## References
- [`WKFrameInfoPrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L37)
- [`WKFrameInfo.mm#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L115)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
