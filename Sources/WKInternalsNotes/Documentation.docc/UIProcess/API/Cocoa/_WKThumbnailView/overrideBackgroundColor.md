# ``WKInternalsNotes/_WKThumbnailView/overrideBackgroundColor``

背景色のオーバーライドを設定する。

## Objective-C Declaration
```objective-c
@property (strong, nonatomic) NSColor *overrideBackgroundColor;
```

## Default Value
`nil` の場合は `quaternaryLabelColor` を使う。

## Discussion
値が変わると `setNeedsDisplay:YES` を行い、`updateLayer` で背景色を反映する。

## References
- [`_WKThumbnailView.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.h#L52)
- [`_WKThumbnailView.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L125)
- [`_WKThumbnailView.mm#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L129)
- [`_WKThumbnailView.mm#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L173)
- [`_WKThumbnailView.mm#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L178)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
