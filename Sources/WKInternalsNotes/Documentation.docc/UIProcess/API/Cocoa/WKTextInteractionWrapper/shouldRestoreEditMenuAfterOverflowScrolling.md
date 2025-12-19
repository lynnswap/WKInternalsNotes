# ``WKInternalsNotes/WKTextInteractionWrapper/shouldRestoreEditMenuAfterOverflowScrolling``

オーバーフロー/スクロール後に edit menu を復元するかどうかのフラグ。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldRestoreEditMenuAfterOverflowScrolling;
```

## Default Value
`NO`（`reset` で明示的に `NO` に戻す）。

## Discussion
`HideEditMenuScope` の生成時に `view.isPresentingEditMenu` を記録し、スコープ終了時に復元するかを判断する。スクロール/ズーム開始時にも同様に使用する。

## References
- [`WKTextInteractionWrapper.mm#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L44)
- [`WKTextInteractionWrapper.mm#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L70)
- [`WKTextInteractionWrapper.mm#L375`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L375)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
