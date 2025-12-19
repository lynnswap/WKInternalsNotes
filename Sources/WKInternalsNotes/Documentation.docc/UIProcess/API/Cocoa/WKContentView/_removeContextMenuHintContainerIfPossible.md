# ``WKInternalsNotes/WKContentView/_removeContextMenuHintContainerIfPossible()``

条件が整った場合にコンテキストメニューヒント用コンテナを削除する。

## Objective-C Declaration
```objective-c
- (void)_removeContextMenuHintContainerIfPossible;
```

## Discussion
リンクプレビューやコンテキストメニュー表示中などの条件をチェックし、不要で空のときにコンテナを削除する。

## References
- [`WKContentViewInteraction.h#L959`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L959)
- [`WKContentViewInteraction.mm#L11822`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L11822)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
