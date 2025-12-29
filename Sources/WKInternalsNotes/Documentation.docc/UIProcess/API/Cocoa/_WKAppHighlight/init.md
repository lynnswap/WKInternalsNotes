# ``WKInternalsNotes/_WKAppHighlight/init()``

公開初期化子としては使用できない。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
`NS_UNAVAILABLE` のため外部からは生成できず、内部の `initWithHighlight:text:image:` が利用される。

## References
- [`_WKAppHighlight.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlight.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
