# ``WKInternalsNotes/WKContentView/dismissFormAccessoryView()``

フォームアクセサリ表示を閉じる。

## Objective-C Declaration
```objective-c
- (void)dismissFormAccessoryView;
```

## Discussion
`dateTimeInputControl` が `dismissWithAnimationForTesting` で閉じられる場合はそこで終了し、それ以外は `accessoryDone` を呼ぶ。watchOS では `dateTimeInputControl` 分岐は無効。

## References
- [`WKContentViewInteraction.h#L1054`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1054)
- [`WKContentViewInteraction.mm#L14683`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14683)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
