# ``WKInternalsNotes/WKContentView/dismissPickersIfNeededWithReason(_:)``

表示中のピッカーやシートを必要に応じて閉じる。

## Objective-C Declaration
```objective-c
- (void)dismissPickersIfNeededWithReason:(WebKit::PickerDismissalReason)reason;
```

## Discussion
ファイルアップロードパネルや共有シート、連絡先ピッカーなどを理由付きで閉じ、閉じた場合は参照を解放する。

## References
- [`WKContentViewInteraction.h#L751`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L751)
- [`WKContentViewInteraction.mm#L9812`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9812)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
