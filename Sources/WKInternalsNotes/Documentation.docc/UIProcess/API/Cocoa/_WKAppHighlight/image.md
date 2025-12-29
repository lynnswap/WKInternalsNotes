# ``WKInternalsNotes/_WKAppHighlight/image``

ハイライトに関連する画像を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, strong) UIImage *image;
```

## Default Value
`nil`（`initWithHighlight:text:image:` で設定される）。

## Discussion
内部で保持している `CocoaImage` をそのまま返す。プラットフォームに応じて `UIImage`/`NSImage` となる。

## References
- [`_WKAppHighlight.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlight.h#L44)
- [`_WKAppHighlight.mm#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAppHighlight.mm#L57)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
