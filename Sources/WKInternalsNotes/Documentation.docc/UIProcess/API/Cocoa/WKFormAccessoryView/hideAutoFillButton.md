# ``WKInternalsNotes/WKFormAccessoryView/hideAutoFillButton()``

AutoFill ボタンを非表示にする。

## Objective-C Declaration
```objective-c
- (void)hideAutoFillButton;
```

## Discussion
ツールバーからボタンを削除し、ユニバーサルコントロールバー利用時はボタングループを隠す。そうでない場合はボタン項目を `nil` にする。

## References
- [`WKFormAccessoryView.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.h#L50)
- [`WKFormAccessoryView.mm#L371`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.mm#L371)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
