# ``WKInternalsNotes/WKContentView/requestTextRecognition(_:imageData:sourceLanguageIdentifier:targetLanguageIdentifier:completionHandler:)``

画像データのテキスト認識を要求する。

## Objective-C Declaration
```objective-c
- (void)requestTextRecognition:(NSURL *)imageURL imageData:(WebCore::ShareableBitmap::Handle&&)imageData sourceLanguageIdentifier:(NSString *)sourceLanguageIdentifier targetLanguageIdentifier:(NSString *)targetLanguageIdentifier completionHandler:(CompletionHandler<void(WebCore::TextRecognitionResult&&)>&&)completion;
```

## Discussion
`ShareableBitmap` と `CGImage` の生成に失敗した場合は空の `TextRecognitionResult` を返す。`ENABLE(IMAGE_ANALYSIS_ENHANCEMENTS)` かつ `targetLanguageIdentifier` が指定されている場合は `requestVisualTranslation` に委譲し、それ以外は `VKAnalysisTypeText` の解析リクエストを `imageAnalyzer` に送って結果を `completion` に渡す。

## References
- [`WKContentViewInteraction.h#L981`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L981)
- [`WKContentViewInteraction.mm#L13038`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13038)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
