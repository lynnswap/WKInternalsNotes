# ``WKInternalsNotes/WKContentView/positionInformation``

現在の位置情報キャッシュを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) const WebKit::InteractionInformationAtPosition& positionInformation;
```

## Default Value
`_positionInformation` を返す。

## Discussion
`InteractionInformationAtPosition` の最新値をそのまま参照で返す。

## References
- [`WKContentViewInteraction.h#L510`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L510)
- [`WKContentViewInteraction.mm#L1916`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1916)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
