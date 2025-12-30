# ``WKInternalsNotes/WKPreviewAction/actionWithIdentifier(_:title:style:handler:)``

`UIPreviewAction` の生成後に `identifier` を保持して返す。

## Objective-C Declaration
```objective-c
+ (instancetype)actionWithIdentifier:(NSString *)identifier title:(NSString *)title style:(UIPreviewActionStyle)style handler:(void (^)(UIPreviewAction *action, UIViewController *previewViewController))handler;
```

## Discussion
`+actionWithTitle:style:handler:` で `WKPreviewAction` を生成し、`identifier` を `_identifier` に保存して返す。

## References
- [`WKPreviewActionItemInternal.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreviewActionItemInternal.h#L35)
- [`WKPreviewActionItem.mm#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreviewActionItem.mm#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
