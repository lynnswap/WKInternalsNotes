# ``WKInternalsNotes/WKActionSheetAssistantDelegate/dataDetectionContextForActionSheetAssistant(_:positionInformation:)``

データ検出用コンテキストを返す。

## Objective-C Declaration
```objective-c
- (NSDictionary *)dataDetectionContextForActionSheetAssistant:(WKActionSheetAssistant *)assistant positionInformation:(const WebKit::InteractionInformationAtPosition&)positionInformation;
```

## Discussion
`dataDetectionContextForPositionInformation:` に処理を委譲し、UI デリゲート由来のコンテキストに前後テキストやプレビュー可否、ソース矩形情報を反映した辞書を返す。

## References
- [`WKActionSheetAssistant.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L73)
- [`WKContentViewInteraction.mm#L10145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10145)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
