# ``WKInternalsNotes/WKContentView/_positionInformationDidChange(_:)``

位置情報更新時の内部処理を行う。

## Objective-C Declaration
```objective-c
- (void)_positionInformationDidChange:(const WebKit::InteractionInformationAtPosition&)info;
```

## Discussion
未処理の位置情報リクエストを解消し、既存キャッシュと `info` をマージして `_positionInformation` を更新する。アクションシートの位置を更新し、待機中ハンドラを実行する。

## References
- [`WKContentViewInteraction.h#L820`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L820)
- [`WKContentViewInteraction.mm#L4141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4141)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
