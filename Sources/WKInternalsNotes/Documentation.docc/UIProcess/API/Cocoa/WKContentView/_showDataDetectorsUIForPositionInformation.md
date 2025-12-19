# ``WKInternalsNotes/WKContentView/_showDataDetectorsUIForPositionInformation(_:)``

位置情報に基づく Data Detectors UI を表示する。

## Objective-C Declaration
```objective-c
- (void)_showDataDetectorsUIForPositionInformation:(const WebKit::InteractionInformationAtPosition&)positionInformation;
```

## Discussion
`WKActionSheetAssistant` に表示を委譲し、位置情報に応じた UI を提示する。

## References
- [`WKContentViewInteraction.h#L858`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L858)
- [`WKContentViewInteraction.mm#L3236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3236)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
