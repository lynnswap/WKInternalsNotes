# ``WKInternalsNotes/WKContentView/accessoryOpen()``

フォームアクセサリの編集を開始する。

## Objective-C Declaration
```objective-c
- (void)accessoryOpen;
```

## Discussion
`_inputPeripheral` が無い場合は何もしない。存在する場合はフォーカス要素を表示し、アクセサリ更新後に `beginEditing` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L871`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L871)
- [`WKContentViewInteraction.mm#L6314`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6314)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
