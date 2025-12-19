# ``WKInternalsNotes/WKContentView/dataDetectionContextForPositionInformation(_:)``

データ検出 UI 用のコンテキスト辞書を構築する。

## Objective-C Declaration
```objective-c
- (NSDictionary *)dataDetectionContextForPositionInformation:(const WebKit::InteractionInformationAtPosition&)positionInformation;
```

## Discussion
UI delegate 由来の辞書をベースにし、DATA_DETECTION 有効時は前後テキストやプレビュー可否を加味して、ソース矩形を反映したコンテキストを返す。

## References
- [`WKContentViewInteraction.h#L857`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L857)
- [`WKContentViewInteraction.mm#L10099`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10099)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
