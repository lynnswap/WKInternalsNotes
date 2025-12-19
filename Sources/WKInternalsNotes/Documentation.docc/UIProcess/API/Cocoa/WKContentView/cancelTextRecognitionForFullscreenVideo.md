# ``WKInternalsNotes/WKContentView/cancelTextRecognitionForFullscreenVideo(_:)``

フルスクリーン動画のテキスト認識をキャンセルする。

## Objective-C Declaration
```objective-c
- (void)cancelTextRecognitionForFullscreenVideo:(AVPlayerViewController *)controller;
```

## Discussion
`ENABLE(IMAGE_ANALYSIS_ENHANCEMENTS)` 有効時に、進行中の解析リクエストがあればキャンセルし、`AVPlayerViewController` に対して `setImageAnalysis:nil` を呼び出して解析結果をクリアする。

## References
- [`WKContentViewInteraction.h#L994`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L994)
- [`WKContentViewInteraction.mm#L13390`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13390)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
