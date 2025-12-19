# ``WKInternalsNotes/WKFormAccessoryView/setNextPreviousItemsVisible(_:)``

前後移動ボタンの表示を切り替える。

## Objective-C Declaration
```objective-c
- (void)setNextPreviousItemsVisible:(BOOL)visible;
```

## Discussion
ユニバーサルコントロールバーではボタングループの表示を切り替え、それ以外では左ツールバーの項目を追加・削除して更新する。

## References
- [`WKFormAccessoryView.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.h#L51)
- [`WKFormAccessoryView.mm#L416`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.mm#L416)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
