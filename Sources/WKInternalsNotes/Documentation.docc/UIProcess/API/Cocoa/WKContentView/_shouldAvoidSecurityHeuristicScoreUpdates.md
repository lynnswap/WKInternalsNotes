# ``WKInternalsNotes/WKContentView/_shouldAvoidSecurityHeuristicScoreUpdates``

セキュリティヒューリスティックスコア更新を避けるべきかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldAvoidSecurityHeuristicScoreUpdates;
```

## Default Value
環境依存（Vision では YES、画像解析の選択中は YES）。

## Discussion
Vision では常に `YES` を返し、画像解析のテキスト選択中であれば `YES` を返す。その他の環境では `NO`。

## References
- [`WKContentViewInteraction.h#L944`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L944)
- [`WKContentViewInteraction.mm#L13490`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13490)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
