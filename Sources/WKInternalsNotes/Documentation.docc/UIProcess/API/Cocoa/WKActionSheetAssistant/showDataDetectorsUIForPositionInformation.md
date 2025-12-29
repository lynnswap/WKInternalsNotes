# ``WKInternalsNotes/WKActionSheetAssistant/showDataDetectorsUIForPositionInformation(_:)``

データ検出結果に基づいてUIを提示する。

## Objective-C Declaration
```objective-c
- (void)showDataDetectorsUIForPositionInformation:(const WebKit::InteractionInformationAtPosition&)positionInformation;
```

## Discussion
DATA_DETECTION 有効時のみ動作する。デリゲートがなければ終了し、`positionInformation` を保持した上で `DataDetection::canBePresentedByDataDetectors` を満たすURLのみ処理する。即時実行可能な場合はデフォルトアクションを実行し、それ以外はアクション一覧を取得してコンテキストメニュー（対応環境）またはアクションシートとして表示する。

## References
- [`WKActionSheetAssistant.h#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L115)
- [`WKActionSheetAssistant.mm#L768`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L768)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
