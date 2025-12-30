# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:showTextForImage:imageURL:title:imageBounds:)``

画像から抽出したテキストを表示する。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistant:(WKActionSheetAssistant *)assistant showTextForImage:(UIImage *)image imageURL:(NSURL *)imageURL title:(NSString *)title imageBounds:(CGRect)imageBounds;
```

## Discussion
`presentVisualSearchPreviewControllerForImage` を呼び、`QLPreviewControllerFirstTimeAppearanceActionEnableVisualSearchDataDetection` を指定してプレビューを表示する。

## References
- [`WKActionSheetAssistant.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L61)
- [`WKContentViewInteraction.mm#L12919`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12919)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
