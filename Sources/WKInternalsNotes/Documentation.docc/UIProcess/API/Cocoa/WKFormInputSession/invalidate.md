# ``WKInternalsNotes/WKFormInputSession/invalidate()``

入力セッションを無効化する。

## Objective-C Declaration
```objective-c
- (void)invalidate;
```

## Discussion
`_contentView` を `nil` に置き換え、入れ替え前の `WKContentView` に対して `_provideSuggestionsToInputDelegate:nil` を呼び出してサジェスト提供を停止する。

## References
- [`WKContentViewInteraction.h#L330`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L330)
- [`WKContentViewInteraction.mm#L898`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L898)
- [`WKContentViewInteraction.mm#L900`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L900)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
