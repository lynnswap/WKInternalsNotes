# ``WKInternalsNotes/WKColorPickerUIMac/didChooseColor(_:)``

ユーザーが色を選択したときの通知を処理する。

## Objective-C Declaration
```objective-c
- (void)didChooseColor:(id)sender;
```

## Discussion
`WKColorPopoverMac` 実装では `sender` が `WKPopoverColorWell` でない場合は無視する。プログラム変更の場合はフラグのみ戻して終了し、ユーザー変更なら `WebColorPickerMac` に選択色を通知する。

## References
- [`WebColorPickerMac.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.h#L52)
- [`WebColorPickerMac.mm#L208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.mm#L208)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
