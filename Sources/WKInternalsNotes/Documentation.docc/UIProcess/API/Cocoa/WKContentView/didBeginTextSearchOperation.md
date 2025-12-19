# ``WKInternalsNotes/WKContentView/didBeginTextSearchOperation()``

テキスト検索開始時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)didBeginTextSearchOperation;
```

## Discussion
検索 UI を表示し、`WebPageProxy` に開始を通知する。

## References
- [`WKContentViewInteraction.h#L987`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L987)
- [`WKContentViewInteraction.mm#L12748`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12748)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
