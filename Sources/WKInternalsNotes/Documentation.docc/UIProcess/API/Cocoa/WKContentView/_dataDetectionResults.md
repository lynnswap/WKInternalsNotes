# ``WKInternalsNotes/WKContentView/_dataDetectionResults()``

データ検出結果を返す。

## Objective-C Declaration
```objective-c
- (NSArray *)_dataDetectionResults;
```

## Discussion
`ENABLE(DATA_DETECTION)` のとき `WebPageProxy::dataDetectionResults()` を返す。

## References
- [`WKContentViewInteraction.h#L847`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L847)
- [`WKContentViewInteraction.mm#L3367`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3367)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
