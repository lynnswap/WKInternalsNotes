# ``WKInternalsNotes/WKContentView/beginTextRecognitionForFullscreenVideo(_:playerViewController:)``

フルスクリーン動画フレームのテキスト認識を開始する。

## Objective-C Declaration
```objective-c
- (void)beginTextRecognitionForFullscreenVideo:(WebCore::ShareableBitmap::Handle&&)imageHandle playerViewController:(AVPlayerViewController *)playerViewController;
```

## Discussion
`ENABLE(IMAGE_ANALYSIS_ENHANCEMENTS)` 有効時に、画像データから `ShareableBitmap` を生成し、`imageAnalyzer` へ解析リクエストを送る。解析結果は `AVPlayerViewController` が `setImageAnalysis:` を実装していれば渡し、同時に `_fullscreenVideoImageAnalysisRequestIdentifier` を管理して二重要求を避ける。

## References
- [`WKContentViewInteraction.h#L993`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L993)
- [`WKContentViewInteraction.mm#L13359`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13359)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
