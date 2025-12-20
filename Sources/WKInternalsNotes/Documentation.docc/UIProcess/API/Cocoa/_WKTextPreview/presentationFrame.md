# ``WKInternalsNotes/_WKTextPreview/presentationFrame``

プレビュー画像の表示フレームを返す。

## Objective-C Declaration
```objective-c
@property (readonly) CGRect presentationFrame;
```

## Default Value
初期化時に渡された `presentationFrame` を保持する。

## Discussion
`initWithSnapshotImage:presentationFrame:` で `_presentationFrame` を設定し、プロパティの合成アクセサで返す。

## References
- [`_WKTextPreview.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextPreview.h#L36)
- [`_WKTextPreview.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextPreview.mm#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
