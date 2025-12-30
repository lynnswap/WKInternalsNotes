# ``WKInternalsNotes/WKSeparatedImageView/initWithCoder(_:)``

`NS_UNAVAILABLE` として利用不可。

## Objective-C Declaration
```objective-c
- (instancetype)initWithCoder:(NSCoder *)coder NS_UNAVAILABLE;
```

## Discussion
公開ソースでは `ASSERT_NOT_REACHED()` のうえ自身を呼び出すスタブ実装。`USE(APPLE_INTERNAL_SDK)` では Swift 実装。

## References
- [`WKSeparatedImageView.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.h#L40)
- [`WKSeparatedImageView.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.mm#L84)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
