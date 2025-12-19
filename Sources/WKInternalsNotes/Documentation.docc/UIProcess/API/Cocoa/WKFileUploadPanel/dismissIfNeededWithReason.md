# ``WKInternalsNotes/WKFileUploadPanel/dismissIfNeededWithReason(_:)``

必要に応じてパネルを閉じる。

## Objective-C Declaration
```objective-c
- (BOOL)dismissIfNeededWithReason:(WebKit::PickerDismissalReason)reason;
```

## Discussion
フルスクリーン表示中のピッカーがあれば閉じない場合がある。理由が `ProcessExited`/`ViewRemoved` の場合は delegate を解除し、終了処理を行う。

## References
- [`WKFileUploadPanel.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.h#L56)
- [`WKFileUploadPanel.mm#L563`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.mm#L563)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
