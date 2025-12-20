# ``WKInternalsNotes/_WKThumbnailView/scale``

サムネイルのスケールを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) CGFloat scale;
```

## Default Value
`initWithFrame:` で 1 に設定される。

## Discussion
値が変わるとスナップショット再取得を要求し、`sublayerTransform` をスケールと `_sublayerTranslation` で更新する。

## References
- [`_WKThumbnailView.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.h#L44)
- [`_WKThumbnailView.mm#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L70)
- [`_WKThumbnailView.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L75)
- [`_WKThumbnailView.mm#L279`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L279)
- [`_WKThumbnailView.mm#L286`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L286)
- [`_WKThumbnailView.mm#L288`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKThumbnailView.mm#L288)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
