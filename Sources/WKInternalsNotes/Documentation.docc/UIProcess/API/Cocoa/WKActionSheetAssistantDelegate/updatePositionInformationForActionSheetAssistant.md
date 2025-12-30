# ``WKInternalsNotes/WKActionSheetAssistantDelegate/updatePositionInformationForActionSheetAssistant(_:)``

位置情報の更新を要求する。

## Objective-C Declaration
```objective-c
- (void)updatePositionInformationForActionSheetAssistant:(WKActionSheetAssistant *)assistant;
```

## Discussion
`_hasValidPositionInformation` を `NO` にし、スナップショット/リンクインジケータ/アニメーション情報付きの `InteractionInformationRequest` を組み立てて非同期更新を要求する。

## References
- [`WKActionSheetAssistant.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L69)
- [`WKContentViewInteraction.mm#L9980`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9980)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
