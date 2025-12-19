# ``WKInternalsNotes/WKContentView/beginTextRecognitionForVideoInElementFullscreen(_:bounds:)``

要素フルスクリーン動画のテキスト認識を開始する。

## Objective-C Declaration
```objective-c
- (void)beginTextRecognitionForVideoInElementFullscreen:(WebCore::ShareableBitmap::Handle&&)bitmapHandle bounds:(WebCore::FloatRect)bounds;
```

## Discussion
`ENABLE(IMAGE_ANALYSIS_ENHANCEMENTS)` 有効時に、フレーム画像から解析リクエストを生成して `imageAnalyzer` に送る。解析成功時は `_imageAnalysisInteractionBounds` を `bounds` に更新し、`installImageAnalysisInteraction:` で解析結果の UI を反映する。

## References
- [`WKContentViewInteraction.h#L997`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L997)
- [`WKContentViewInteraction.mm#L13410`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13410)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
