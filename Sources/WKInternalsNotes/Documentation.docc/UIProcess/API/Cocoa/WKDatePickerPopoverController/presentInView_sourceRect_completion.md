# ``WKInternalsNotes/WKDatePickerPopoverController/presentInView(_:sourceRect:completion:)``

日付選択 UI を指定のビューから表示する。

## Objective-C Declaration
```objective-c
- (void)presentInView:(UIView *)view sourceRect:(CGRect)rect completion:(void(^)())completion;
```

## Discussion
全画面プレゼンテーション用の `UIViewController` を取得し、`isBeingDismissed` の場合は `presentingViewController` を辿って安全なコントローラを探す。見つからなければ `completion` を即時実行する。表示前に `_canSendPopoverControllerDidDismiss` を有効化し、ウィンドウ内の空き領域からポップオーバーの矢印方向を計算して `permittedArrowDirections` を設定する。最後に `sourceView`/`sourceRect` をセットして `presentViewController` で表示する。

## References
- [`WKDatePickerPopoverController.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.h#L44)
- [`WKDatePickerPopoverController.mm#L437`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKDatePickerPopoverController.mm#L437)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
