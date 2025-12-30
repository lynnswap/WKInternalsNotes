# ``WKInternalsNotes/WKSeparatedImageView/setSurface(_:)``

描画用の `IOSurface` を設定する。

## Objective-C Declaration
```objective-c
- (void)setSurface:(nullable IOSurfaceRef)surface;
```

## Discussion
公開ソースでは no-op。`USE(APPLE_INTERNAL_SDK)` では Swift 実装。

## References
- [`WKSeparatedImageView.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.h#L42)
- [`WKSeparatedImageView.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKSeparatedImageView.mm#L90)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
