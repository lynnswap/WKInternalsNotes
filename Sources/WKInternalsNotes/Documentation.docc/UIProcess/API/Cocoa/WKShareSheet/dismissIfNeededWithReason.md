# ``WKInternalsNotes/WKShareSheet/dismissIfNeededWithReason(_:)``

必要に応じて共有シートを閉じる。

## Objective-C Declaration
```objective-c
- (BOOL)dismissIfNeededWithReason:(WebKit::PickerDismissalReason)reason;
```

## Discussion
理由に応じて delegate を解除し、共有シートを閉じる。iOS ではフルスクリーン表示中のケースを考慮してキャンセルを見送る場合がある。

## References
- [`WKShareSheet.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.h#L47)
- [`WKShareSheet.mm#L500`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.mm#L500)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
