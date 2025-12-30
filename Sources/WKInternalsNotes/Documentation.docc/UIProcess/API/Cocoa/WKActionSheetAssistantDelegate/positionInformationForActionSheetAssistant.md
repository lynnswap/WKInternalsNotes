# ``WKInternalsNotes/WKActionSheetAssistantDelegate/positionInformationForActionSheetAssistant(_:)``

現在位置のインタラクション情報を返す。

## Objective-C Declaration
```objective-c
- (std::optional<WebKit::InteractionInformationAtPosition>)positionInformationForActionSheetAssistant:(WKActionSheetAssistant *)assistant;
```

## Discussion
`InteractionInformationRequest` を構築し、スナップショット/リンクインジケータ/アニメーション情報を取得する。`ensurePositionInformationIsUpToDate` が失敗した場合は `std::nullopt`、成功時は `_positionInformation` を返す。

## References
- [`WKActionSheetAssistant.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L58)
- [`WKContentViewInteraction.mm#L9966`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9966)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
