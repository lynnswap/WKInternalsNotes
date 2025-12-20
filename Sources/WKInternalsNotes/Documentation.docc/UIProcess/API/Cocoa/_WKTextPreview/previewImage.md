# ``WKInternalsNotes/_WKTextPreview/previewImage``

プレビュー画像を返す。

## Objective-C Declaration
```objective-c
@property (readonly) CGImageRef previewImage;
```

## Default Value
初期化時に渡された `snapshotImage` を保持する。

## Discussion
`initWithSnapshotImage:presentationFrame:` で保持した `_previewImage` をそのまま返す。

## References
- [`_WKTextPreview.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextPreview.h#L33)
- [`_WKTextPreview.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextPreview.mm#L39)
- [`_WKTextPreview.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextPreview.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
