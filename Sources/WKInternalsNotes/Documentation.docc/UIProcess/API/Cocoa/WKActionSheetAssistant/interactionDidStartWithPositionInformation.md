# ``WKInternalsNotes/WKActionSheetAssistant/interactionDidStartWithPositionInformation(_:)``

データ検出のインタラクション開始を通知する。

## Objective-C Declaration
```objective-c
- (void)interactionDidStartWithPositionInformation:(const WebKit::InteractionInformationAtPosition&)information;
```

## Discussion
DATA_DETECTION 有効時のみ動作する。デリゲートが存在し、URLがデータ検出対象である場合に `DDDetectionController` の `interactionDidStartForURL:` を呼ぶ。

## References
- [`WKActionSheetAssistant.h#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L124)
- [`WKActionSheetAssistant.mm#L298`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L298)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
