# ``WKInternalsNotes/WKContentView/cancelTextRecognitionForVideoInElementFullscreen()``

要素フルスクリーン動画のテキスト認識をキャンセルする。

## Objective-C Declaration
```objective-c
- (void)cancelTextRecognitionForVideoInElementFullscreen;
```

## Discussion
`ENABLE(IMAGE_ANALYSIS_ENHANCEMENTS)` 有効時に `installImageAnalysisInteraction:` で導入した UI を外し、進行中の解析リクエストがあればキャンセルする。

## References
- [`WKContentViewInteraction.h#L998`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L998)
- [`WKContentViewInteraction.mm#L13438`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13438)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
