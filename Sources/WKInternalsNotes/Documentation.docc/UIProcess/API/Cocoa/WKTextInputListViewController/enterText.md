# ``WKInternalsNotes/WKTextInputListViewController/enterText(_:)``

テキスト入力を delegate に通知する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)enterText:(NSString *)text;
```

## Discussion
`text` を `NSAttributedString` に変換し、`quickboard:textEntered:` を通じて delegate に通知する（deprecated API を使用）。

## References
- [`WKTextInputListViewController.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L66)
- [`WKTextInputListViewController.mm#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L127)
- [`WKTextInputListViewController.mm#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L130)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
