# ``WKInternalsNotes/WKContentView/ensurePositionInformationIsUpToDate(_:)``

位置情報が最新であることを同期的に保証する。

## Objective-C Declaration
```objective-c
- (BOOL)ensurePositionInformationIsUpToDate:(WebKit::InteractionInformationRequest)request;
```

## Discussion
最新情報が無い場合、Web プロセスが利用可能なら非同期更新を要求して同期待機し、応答に応じて `_hasValidPositionInformation` を更新して返す。

## References
- [`WKContentViewInteraction.h#L882`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L882)
- [`WKContentViewInteraction.mm#L3284`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3284)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
