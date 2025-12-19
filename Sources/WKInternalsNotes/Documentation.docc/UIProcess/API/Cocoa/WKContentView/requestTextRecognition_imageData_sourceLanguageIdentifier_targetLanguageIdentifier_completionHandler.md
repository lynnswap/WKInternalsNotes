# ``WKInternalsNotes/WKContentView/requestTextRecognition(_:imageData:sourceLanguageIdentifier:targetLanguageIdentifier:completionHandler:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)requestTextRecognition:(NSURL *)imageURL imageData:(WebCore::ShareableBitmap::Handle&&)imageData sourceLanguageIdentifier:(NSString *)sourceLanguageIdentifier targetLanguageIdentifier:(NSString *)targetLanguageIdentifier completionHandler:(CompletionHandler<void(WebCore::TextRecognitionResult&&)>&&)completion;
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`WKContentViewInteraction.h#L981`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L981)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
