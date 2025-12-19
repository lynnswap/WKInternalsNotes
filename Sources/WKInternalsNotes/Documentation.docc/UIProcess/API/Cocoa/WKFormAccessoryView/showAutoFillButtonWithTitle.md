# ``WKInternalsNotes/WKFormAccessoryView/showAutoFillButtonWithTitle(_:)``

AutoFill ボタンを表示する。

## Objective-C Declaration
```objective-c
- (void)showAutoFillButtonWithTitle:(NSString *)title;
```

## Discussion
AutoFill ボタンが未生成なら生成してタイトルを設定し、ユニバーサルコントロールバー利用時はグループを表示してレイアウトを更新する。

## References
- [`WKFormAccessoryView.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.h#L49)
- [`WKFormAccessoryView.mm#L386`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.mm#L386)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
