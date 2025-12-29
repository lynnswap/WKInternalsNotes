# ``WKInternalsNotes/WKDatePickerPopoverController/assertAccessoryViewCanBeHitTestedForTesting()``

アクセサリービューへのヒットテスト可否を検証する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)assertAccessoryViewCanBeHitTestedForTesting;
```

## Discussion
`accessoryView` と `viewIfLoaded` の存在を `RELEASE_ASSERT` で確認し、アクセサリービューの中心点がヒットテストで取得できるかを検証する。ヒットテストの結果がアクセサリービュー階層に到達しなければ `RELEASE_ASSERT` で失敗させる。

## References
- [`WKDatePickerPopoverController.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.h#L46)
- [`WKDatePickerPopoverController.mm#L285`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.mm#L285)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
