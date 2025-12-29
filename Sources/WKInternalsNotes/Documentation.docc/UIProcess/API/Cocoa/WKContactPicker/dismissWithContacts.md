# ``WKInternalsNotes/WKContactPicker/dismissWithContacts(_:)``

テスト用に指定した連絡先でピッカーを閉じる。

## Objective-C Declaration
```objective-c
- (void)dismissWithContacts:(NSArray *)contacts;
```

## Discussion
`CNContactPickerViewController` をアニメーションなしで閉じ、`contacts` を `CNContact` に変換して `didSelectContacts:` を呼び出す。

## References
- [`WKContactPicker.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.h#L64)
- [`WKContactPicker.mm#L255`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.mm#L255)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
