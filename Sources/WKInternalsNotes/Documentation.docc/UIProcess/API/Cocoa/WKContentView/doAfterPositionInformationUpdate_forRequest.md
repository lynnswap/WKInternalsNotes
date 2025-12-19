# ``WKInternalsNotes/WKContentView/doAfterPositionInformationUpdate(_:forRequest:)``

位置情報が更新された後にコールバックを実行する。

## Objective-C Declaration
```objective-c
- (void)doAfterPositionInformationUpdate:(void (^)(WebKit::InteractionInformationAtPosition))action forRequest:(WebKit::InteractionInformationRequest)request;
```

## Discussion
現在の位置情報がリクエストに対して有効なら即時実行し、そうでなければ保留キューに追加して非同期の更新を要求する。

## References
- [`WKContentViewInteraction.h#L881`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L881)
- [`WKContentViewInteraction.mm#L3270`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3270)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
