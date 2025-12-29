# ``WKInternalsNotes/WKFormPeripheralBase/singleTapShouldEndEditing``

単一タップで編集を終了するかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL singleTapShouldEndEditing;
```

## Default Value
`NO`。

## Discussion
`WKContentViewInteraction` の単一タップ処理で参照され、`YES` の場合は `endEditing` が呼ばれる。

## References
- [`WKContentViewInteraction.mm#L4038`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4038)
- [`WKFormPeripheralBase.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormPeripheralBase.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
