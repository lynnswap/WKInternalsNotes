# ``WKInternalsNotes/WKTimePickerViewController/delegate``

クイックボードのデリゲート。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKQuickboardViewControllerDelegate> delegate;
```

## Default Value
`nil`。

## Discussion
初期値の取得や `Cancel/Set` 操作の通知に使われる。`@dynamic` としてスーパークラスの実装を利用している。

## References
- [`WKTimePickerViewController.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTimePickerViewController.h#L32)
- [`WKTimePickerViewController.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTimePickerViewController.mm#L52)
- [`WKTimePickerViewController.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTimePickerViewController.mm#L84)
- [`WKTimePickerViewController.mm#L137`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKTimePickerViewController.mm#L137)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
