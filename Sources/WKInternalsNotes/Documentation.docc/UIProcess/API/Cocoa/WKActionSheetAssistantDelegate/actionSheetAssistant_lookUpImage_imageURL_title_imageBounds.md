# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:lookUpImage:imageURL:title:imageBounds:)``

画像のビジュアル検索プレビューを表示する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistant:(WKActionSheetAssistant *)assistant lookUpImage:(UIImage *)image imageURL:(NSURL *)imageURL title:(NSString *)title imageBounds:(CGRect)imageBounds;
```

## Discussion
`presentVisualSearchPreviewControllerForImage` を呼び、`QLPreviewControllerFirstTimeAppearanceActionEnableVisualSearchMode` を指定してプレビューを表示する。

## References
- [`WKActionSheetAssistant.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L63)
- [`WKContentViewInteraction.mm#L12929`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12929)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
