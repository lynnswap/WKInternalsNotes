# ``WKInternalsNotes/_WKUserStyleSheet/forMainFrameOnly``

メインフレームのみへ注入するかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isForMainFrameOnly) BOOL forMainFrameOnly;
```

## Discussion
`UserStyleSheet` の `injectedFrames` が `InjectInTopFrameOnly` かどうかを返す。

## References
- [`_WKUserStyleSheet.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.h#L47)
- [`_WKUserStyleSheet.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserStyleSheet.mm#L84)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
