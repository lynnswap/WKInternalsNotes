# ``WKInternalsNotes/WKFrameInfo/_parentFrameHandle``

親フレームの _WKFrameHandle を返す（存在しなければ nil）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy, nullable) _WKFrameHandle *_parentFrameHandle WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
`self._protectedFrameInfo->parentFrameHandle()` をラップした `_WKFrameHandle`。

## Discussion
親がない場合は `parentFrameHandle()` が null となり、`wrapper(...)` の結果は `nil` になる。

## References
- [`WKFrameInfoPrivate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L35)
- [`WKFrameInfo.mm#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L105)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
