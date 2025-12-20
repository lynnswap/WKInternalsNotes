# ``WKInternalsNotes/WKPasswordView/showPasswordFailureAlert()``

パスワード失敗時のアラートを表示する。

## Objective-C Declaration
```objective-c
- (void)showPasswordFailureAlert;
```

## Discussion
パスワード入力フィールドをクリアし、失敗メッセージを持つ `UIAlertController` を生成して OK ボタンを追加する。`rootViewController` からアラートを表示する。

## References
- [`WKPasswordView.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.h#L35)
- [`WKPasswordView.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L123)
- [`WKPasswordView.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L125)
- [`WKPasswordView.mm#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKPasswordView.mm#L132)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
