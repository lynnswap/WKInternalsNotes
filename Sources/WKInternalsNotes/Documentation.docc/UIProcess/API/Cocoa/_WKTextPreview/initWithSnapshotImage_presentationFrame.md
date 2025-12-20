# ``WKInternalsNotes/_WKTextPreview/initWithSnapshotImage(_:presentationFrame:)``

スナップショット画像と表示フレームを設定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithSnapshotImage:(CGImageRef)snapshotImage presentationFrame:(CGRect)presentationFrame;
```

## Discussion
`[self init]` が失敗した場合は `nil` を返す。成功時は `snapshotImage` を保持し、`presentationFrame` を `_presentationFrame` に設定する。

## References
- [`_WKTextPreview.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextPreview.h#L38)
- [`_WKTextPreview.mm#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextPreview.mm#L34)
- [`_WKTextPreview.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextPreview.mm#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
