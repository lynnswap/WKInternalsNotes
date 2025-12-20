# ``WKInternalsNotes/WKImagePreviewViewController/initWithCGImage(_:defaultActions:elementInfo:)``

CGImage からプレビュー表示用のビューコントローラを初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithCGImage:(RetainPtr<CGImageRef>)image defaultActions:(RetainPtr<NSArray>)actions elementInfo:(RetainPtr<_WKActivatedElementInfo>)elementInfo;
```

## Discussion
`initWithNibName:bundle:` を `nil` で初期化した後、`_image` を保持し、`UIImageView` を生成して `UIViewContentModeScaleAspectFill` を設定する。`CGImage` から `UIImage` を作成して設定し、画面サイズに収まるよう `_scaleSizeWithinSize` で算出したサイズを `preferredContentSize` と `imageView` の frame に反映する。最後に `actions` と `elementInfo` を `_imageActions` / `_activatedElementInfo` として保持する。

## References
- [`WKImagePreviewViewController.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKImagePreviewViewController.h#L41)
- [`WKImagePreviewViewController.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKImagePreviewViewController.mm#L47)
- [`WKImagePreviewViewController.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKImagePreviewViewController.mm#L55)
- [`WKImagePreviewViewController.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKImagePreviewViewController.mm#L64)
- [`WKImagePreviewViewController.mm#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WKImagePreviewViewController.mm#L68)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
