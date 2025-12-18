# ``WKInternalsNotes/WKURLSchemeTaskPrivate/_frame``

URL scheme task に対応するフレーム情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKFrameInfo *_frame WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
URL scheme task に紐づく `WKFrameInfo` を返すため固定のデフォルト値はない。

## Discussion
`_urlSchemeTask->frameInfo()` の結果を `WKFrameInfo` にラップして返す。

## References
- [`WKURLSchemeTaskPrivate.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKURLSchemeTaskPrivate.h#L50)
- [`WKURLSchemeTask.mm#L168`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKURLSchemeTask.mm#L168)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
