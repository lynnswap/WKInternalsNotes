# ``WKInternalsNotes/WKFrameInfo/_title``

フレームのタイトルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy, nullable) NSString *_title WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Default Value
`self._protectedFrameInfo->title().createNSString()` の結果。

## Discussion
API::FrameInfo の `title()` を `NSString` に変換して返す。

## References
- [`WKFrameInfoPrivate.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L41)
- [`WKFrameInfo.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L135)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
