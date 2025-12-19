# ``WKInternalsNotes/WKContentView/_dismissContactPickerWithContacts(_:)``

連絡先ピッカーを指定連絡先で閉じる。

## Objective-C Declaration
```objective-c
- (void)_dismissContactPickerWithContacts:(NSArray *)contacts;
```

## Discussion
ContactsUI が有効な場合に `_contactPicker` へ `dismissWithContacts:` を委譲する。

## References
- [`WKContentViewInteraction.h#L1041`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1041)
- [`WKContentViewInteraction.mm#L14635`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14635)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
