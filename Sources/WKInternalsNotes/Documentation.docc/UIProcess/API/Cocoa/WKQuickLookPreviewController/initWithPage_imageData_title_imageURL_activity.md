# ``WKInternalsNotes/WKQuickLookPreviewController/initWithPage(_:imageData:title:imageURL:activity:)``

Quick Look 用のプレビュー項目を構築する初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)initWithPage:(WebKit::WebPageProxy&)page imageData:(NSData *)data title:(NSString *)title imageURL:(NSURL *)imageURL activity:(WebKit::QuickLookPreviewActivity)activity;
```

## Discussion
`_activity` と `_imageData` を保持し、`QLItem` を `UTTypePNG` と `title` で生成する。`setPreviewOptions:` が使える場合は `imageURL` と `page.currentURL()` から作った `pageURL` を辞書に設定する。

## References
- [`WKQuickLookPreviewController.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.h#L40)
- [`WKQuickLookPreviewController.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKQuickLookPreviewController.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
