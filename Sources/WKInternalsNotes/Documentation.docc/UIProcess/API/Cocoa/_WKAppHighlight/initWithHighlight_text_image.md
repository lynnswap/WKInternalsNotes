# ``WKInternalsNotes/_WKAppHighlight/initWithHighlight(_:text:image:)``

ハイライト情報を保持する内部初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)initWithHighlight:(NSData *)highlight text:(NSString *)text image:(CocoaImage *)image;
```

## Discussion
`highlight`、`text`、`image` をそのまま保持する。

## References
- [`_WKAppHighlightInternal.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlightInternal.h#L30)
- [`_WKAppHighlight.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlight.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
