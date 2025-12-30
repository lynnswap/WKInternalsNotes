# ``WKInternalsNotes/WKSeparatedImageView/init()``

`CGRectZero` で初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_DESIGNATED_INITIALIZER;
```

## Discussion
`USE(APPLE_INTERNAL_SDK)` では Swift 実装。公開ソースでは `initWithFrame:CGRectZero` を呼ぶ。

## References
- [`WKSeparatedImageView.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.h#L39)
- [`WKSeparatedImageView.mm#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.mm#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
