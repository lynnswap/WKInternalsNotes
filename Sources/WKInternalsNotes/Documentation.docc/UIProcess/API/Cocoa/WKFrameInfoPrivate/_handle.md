# ``WKInternalsNotes/WKFrameInfo/_handle``

フレーム識別子を持つ _WKFrameHandle を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) _WKFrameHandle *_handle WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
`self._protectedFrameInfo->handle()` をラップした `_WKFrameHandle`。

## Discussion
API::FrameInfo の `handle()` を `wrapper(...)` で Objective-C ラッパー化し、`autorelease` して返す。

## References
- [`WKFrameInfoPrivate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L34)
- [`WKFrameInfo.mm#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L100)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
