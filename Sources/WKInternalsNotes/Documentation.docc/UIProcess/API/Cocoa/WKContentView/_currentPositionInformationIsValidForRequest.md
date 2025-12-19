# ``WKInternalsNotes/WKContentView/_currentPositionInformationIsValidForRequest(_:)``

現在の位置情報がリクエストに対して有効か判定する。

## Objective-C Declaration
```objective-c
- (BOOL)_currentPositionInformationIsValidForRequest:(const WebKit::InteractionInformationRequest&)request;
```

## Discussion
`_hasValidPositionInformation` とリクエストの一致判定の両方を満たす場合に `YES` を返す。

## References
- [`WKContentViewInteraction.h#L821`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L821)
- [`WKContentViewInteraction.mm#L3320`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3320)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
