# ``WKInternalsNotes/WKTextInputListViewController/updateTextSuggestions(_:)``

テキストサジェスト一覧を更新する。

## Objective-C Declaration
```objective-c
- (void)updateTextSuggestions:(NSArray<UITextSuggestion *> *)suggestions;
```

## Discussion
`suggestions` の `displayText` から `NSAttributedString` を作成し、`messages` に設定する。

## References
- [`WKTextInputListViewController.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.h#L57)
- [`WKTextInputListViewController.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L117)
- [`WKTextInputListViewController.mm#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTextInputListViewController.mm#L124)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
